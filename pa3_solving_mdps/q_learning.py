
from pa3_solving_mdps.mdp_state import MDPState
from typing import Dict, List
import random


class QLearning:
    '''Q-Learning Class, holds all logic for Q-Learning
    '''

    def __init__(self,  mdpStates: Dict[str, MDPState], alpha: float=0.1, lam: float=0.99, maxChangeThreshold: float=0.001, alphaChangeRate: float=0.99) -> None:
        '''Constructor for QLearning class.

        Args:
            mdpStates (Dict[str, MDPState]): The modeld MDP.
            alpha (float, optional): The alpha, aka, the Learning Rate. Defaults to 0.1.
            lam (float, optional): The lambda, aka, the Discount Rate.. Defaults to 0.99.
            maxChangeThreshold (float, optional): The maximum change between q-values that will cause the algorithm to stop. Defaults to 0.001.
            alphaChangeRate (float, optional): The rate and which alpha will change after each episode (alpha = alpha * alphaChangeRate). Defaults to 0.99.
        '''
        self.mdpStates = mdpStates
        # Learning rate.
        self.alpha: float = alpha
        # Dicount rate.
        self.lam: float = lam
        # The max change before we stop.
        self.maxChangeThreshold = maxChangeThreshold
        # The rate of change for alpha. alpha = alpha * alphaChangeRate
        self.alphaChangeRate = alphaChangeRate
        

    def qLearningAlg(self, startStateName: str, endStateName: str) -> None:
        '''The actual Q-Learning algorithm.

        Args:
            startStateName (str): The name of the start state.
            endStateName (str): The name of the end state.
        '''

        # Flag for if we meat the threshold.
        thresholdMet: bool = False
        # The number of episodes.
        episodeCount: int = 0
        # Keep going until we reach the threshold for stopping the algoirhtm.
        while (thresholdMet is False):

            # At the beginning of each episode, go to the starting state.
            currentState: MDPState = self.mdpStates.get(startStateName)
            # Go through the MDP until we reach the end state. THis will be an episode.
            while (currentState.name != endStateName):
                print("____State: " + currentState.name + "____")

                # Pick a random action from the current state.
                randAction: str = MDPState.pickRandAction(currentState)

                # Get the reward for that action.
                actionRewards: List[int] = currentState.getActionRewards(randAction)
                
                # Get the next state name for taking that action at our current state. 
                nextStateName: str = currentState.getActionNextStates(randAction)[0]
                # Get the actual state object using the state name.
                nextState: MDPState = self.mdpStates.get(nextStateName)

                # If the next state is the end state, there is no calculations that can be done so we move on to the next episode.
                if (nextState.name == "11aCB"):
                    break
                
                # Get the q value for the current state/action pair.
                newQvalue: float = self.qValue(currentState, randAction, nextState)

                # Print the details for this episode.
                print("Action Taken: " + randAction)
                print("Reward: " + str(actionRewards[0]))
                print("Prev. Q Value: " + str(currentState.getActionQValues(randAction)[0]))
                print("New Q Value: " + str(newQvalue))

                # If the change between the new q-value and the old q-vlaue is less than the max alpha change, we end the algorithm.
                if (newQvalue - currentState.getActionQValues(randAction)[0] < self.maxChangeThreshold):
                    print("CHANGE LESS THAN 0.001")
                    thresholdMet = True
                    break
                
                # Update the state/action pairs q-value.
                currentState.setActionQValue(randAction, newQvalue, 0)

                # Go to the next state.
                currentState = self.mdpStates.get(currentState.getActionNextStates(randAction)[0])

            print("End of episode " + str(episodeCount) + ".")
            # After each episode, make the alpha smaller.
            self.alpha = self.alpha * self.alphaChangeRate
            # Increment episdoe counter.
            episodeCount += 1
        
        # Finally, when we are done with the algorithm, print out all the details.
        print()
        print("*****FINAL RESULTS*****")
        self.printAllQValues()
        print()
        print("Number of Episodes: " + str(episodeCount))
        print("Optimal Path: " + str(self.getOptimalPath(startStateName, endStateName)))
                
        

    def temporalDifference(self, currentState: MDPState, action: str, nextState: MDPState) -> float:
        '''Calculates the temporal difference of the state/action pair.

        Args:
            currentState (MDPState): The current state we are at.
            action (str): The action we took in the current state.
            nextState (MDPState): The next state for preforming the state/action pair.

        Returns:
            float: The temporal difference of the state/action pair.
        '''
        # First, we need to get the list of all q-values from the next state.
        listOfActionsRewards: List[int] = []
        actionName: str
        for actionName in nextState.actions.keys():
            listOfActionsRewards.append(nextState.getActionRewards(actionName)[0])
        
        return currentState.getActionRewards(action)[0] + (self.lam * max(listOfActionsRewards) - currentState.getActionQValues(action)[0])
    
    def qValue(self, currentState: MDPState, action: str, nextState: MDPState) -> float:
        '''Calculates the q-value for the state/action pair.

        Args:
            currentState (MDPState): The current state we are at.
            action (str): The action we took in the current state.
            nextState (MDPState): The next state for taking action and the current state.

        Returns:
            float: The q-value for the action/pair.
        '''
        return currentState.getActionQValues(action)[0] + (self.alpha * self.temporalDifference(currentState, action, nextState))

    def getOptimalPath(self, startStateName: str, endStateName: str) -> List[str]:
        '''Returns the shortest state path as a list by getting the best q-values.

        Args:
            startStateName (str): The starting state name.
            endStateName (str): The endind state name.

        Returns:
            List[str]: The best path from the starting state to the end state as a list.
        '''
        # List to hold our path.
        shortestPath: List[str] = []
        currentState: MDPState = self.mdpStates.get(startStateName)

        # Put the starting state in the path.
        shortestPath.append(currentState.name)

        # Go through the MDP while we have not reached the end.
        while (currentState.name != endStateName):
            # Gets the best q-value action from the current state.
            bestAction: str = MDPState.getBestQValueAction(currentState)

            # Set the current state by using the action with the best q-value.
            currentState = self.mdpStates.get(currentState.getActionNextStates(bestAction)[0])
            # Add that state to the path.
            shortestPath.append(currentState.name)

        return shortestPath

    def printAllQValues(self) -> None:
        '''Prints out all the q-values for the MDP.
        '''
        
        stateName: str
        for stateName in self.mdpStates.keys():
            state: MDPState = self.mdpStates.get(stateName)
            # print("____State: " + state.name + "____")
            print("____State: {}".format(stateName) + "____")
            
            action: str
            for action in state.actions.keys():
                print("Action: {}".format(action) + "    Q-Value: {:.4f}".format(state.getActionQValues(action)[0]))
                # print("Action: " + action + "    Q-Value: " + str(state.getActionQValues(action)[0]))
            
            







# Work of: Timothy P. McCrary, Jesus M. Hernandez
