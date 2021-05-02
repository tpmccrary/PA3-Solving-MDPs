from typing import Dict, List
from pa3_solving_mdps.mdp_state import MDPState
import random

# python3 -m pydoc -w <file_name>.py

class MonteCarlo:
    '''The Monte Carlo algorithm for the MDP.
    '''

    def __init__(self, mdpStates: Dict[str, MDPState]) -> None:
        '''Constructor for a new MonteCarlo object.

        Args:
            mdpStates (Dict[str, MDPState]): The modeled MDP as a dictionary(hashtable).
        '''

        # The MDP modled in a dictionary.
        self.mdpStates: Dict[str, MDPState] = mdpStates
        # The alpha rate for the value funciton.
        self.alpha: float = 0.1
        # The total reward for an episode.
        self.totalReward: int = 0
        # The list of total rewards for each episode.
        self.episodeRewards: List[int] = []
        # The state path for an episode
        self.statePath: List[str] = []
        # The action path for an episode.
        self.actionPath: List[str] = []
        # The reward path for an episode.
        self.rewardPath: List[int] = []

    # The Monte Carlo algorithm.
    def monteCarloAlg(self) -> None:
        '''Performs 50 episodes on the MDP.
        '''

        # Do 50 episodes. 1 episode is going from the start state to the end state.
        for i in range(50):

            # Every episode, start at the beginning. State RU8p.
            currentState: MDPState = self.mdpStates.get("RU8p")

            # Go through the MDP until we reach the end, state 11aCB. This is 1 episode.
            while (currentState.name != "11aCB"):
             
                # Pick a random action from the current state.
                randAction: str = self.pickRandAction(currentState)

                # Get the possible rewards for that action.
                actionRewards: List[int] = currentState.getActionRewards(randAction)

                # If there are multiple rewards for one action, that means the action splits into two different paths.
                # So, pick a random reward path to go down.
                actionPath: int = 0
                if (len(actionRewards) > 1):
                    actionPath: int = random.randint(0, len(actionRewards) - 1)

                # Add this reward to the rolling sum of rewards.
                self.totalReward += actionRewards[actionPath]

                # Record the paths for the states, the actions, and the rewards.
                self.statePath.append(currentState.name)
                self.actionPath.append(randAction)
                self.rewardPath.append(actionRewards[actionPath])

                # Get the next state from the given action and the actions path.
                currentState = self.mdpStates[currentState.getActionNextStates(randAction)[actionPath]] 

            # We have reached the end of an episode.
            # Update the states that were visited in the episode.
            self.updateStatesInEpisode(self.mdpStates, self.statePath)

            self.episodeRewards.append(self.totalReward)
            
            # Print out what happened in that episode.
            self.printEpisode(i, self.statePath, self.actionPath, self.rewardPath, self.totalReward)
            # Reset everything for the new, upcoming, episode.
            self.statePath = []
            self.actionPath = []
            self.rewardPath = []
            self.totalReward = 0

        # Finally, when we have done all 50 episodes, print the MDPs state values and the average reward for each episode.
        self.printStatesValues(self.mdpStates)
        self.printAverageReward(self.episodeRewards)
       

    def pickRandAction(self, state: MDPState) -> str:
        '''Given a state, returns a random action from that state.

        Args:
            state (MDPState): The state.

        Returns:
            str: A random action from state.
        '''
        return random.choice(list(state.actions))

    def updateStatesInEpisode(self, mdpStates: Dict[str, MDPState], stateList: List[str]) -> None:
        '''Given an MDP and a state path, update all the states in the MDP given that path.

        Args:
            mdpStates (Dict[str, MDPState]): The MDP.
            stateList (List[str]): The list of states.
        '''
        stateName: str
        for stateName in stateList:
                self.updateStateValue(mdpStates.get(stateName))
    
    def updateStateValue(self, state: MDPState) -> None:
        '''Given a state from the MDP, update its value using: V(S) = V(S) + alpha * [R - V(S)].

        Args:
            state (MDPState): The state.
        '''
        state.value = state.value + self.alpha * (self.totalReward - state.value)


    def printStatesValues(self, mdpStates: Dict[str, MDPState]) -> None:
        '''Given an MDP, prints all its states and their values.

        Args:
            mdpStates (Dict[str, MDPState]): The MDP that is printed.
        '''
        stateName: str
        for stateName in mdpStates.keys():
            print(stateName + ": " + str(mdpStates.get(stateName).value))
    
    def printAverageReward(self, episodeRewards: List[int]) -> None:
        '''Given a list of rewards, prints the average of those rewards.

        Args:
            episodeRewards (List[int]): The list of rewards to average.
        '''
        sum: int = 0
        reward: int
        for reward in episodeRewards:
            sum += reward
        sum = sum / len(episodeRewards)
        print("Average Episode Reward: " + str(sum))

    def printEpisode(self, i: int, statePath: List[str], actionPath: List[str], rewardPath: List[int], totalReward: List[int]) -> None:
        '''Prints the information about the episode, namely: the episodes paths and total reward.

        Args:
            i (int): The episode number.
            statePath (List[str]): The path of states.
            actionPath (List[str]): The path of actions.
            rewardPath (List[int]): The path of rewards.
            totalReward (List[int]): The total reward for that episode.
        '''

        print("____Epidsode " + str(i) + "____")
        # print("State: " + currentState.name + "    Value: " + str(currentState.value))
        print("State Path: " + str(self.statePath))
        print("Action Path: " + str(self.actionPath))
        print("Reward Path: " + str(self.rewardPath))
        print("Total Reward: " + str(self.totalReward))
        
# Work of: Timothy P. McCrary, Jesus M. Hernandez
        
