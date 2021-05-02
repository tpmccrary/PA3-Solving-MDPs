import random

class MonteCarlo:

    def __init__(self, mdpStates) -> None:
        print("This is the MonteCarlo class.")
        # The model of the MDP as a hashtable.
        self.mdpStates = mdpStates
        self.alpha = 0.1
        # The total reward for the episode.
        self.totalReward = 0
        # The 
        self.episodeRewards = []
        self.statePath = []
        self.actionPath = []
        self.rewardPath = []

    # The Monte Carlo algorithm.
    def monteCarloAlg(self):

        # Do 50 episodes.
        for i in range(50):

            currentState = self.mdpStates.get("RU8p")

            while (currentState.name is not "11aCB"):
                # Update current state value.
                # self.updateStateValue(currentState)

                # Pick a random action from the current state.
                randAction = self.pickRandAction(currentState)

                # Get the possible rewards for that action.
                actionRewards = currentState.getActionRewards(randAction)
                
                pathIndex = 0

                # If there are multiple rewards for one action, that means they split.
                # So, pick a random reward path to go down.
                if (len(actionRewards) > 1):
                    pathIndex = random.randint(0, len(actionRewards) - 1)

                # Add this reward to the rolling sum of rewards.
                self.totalReward += actionRewards[pathIndex]

                # Add the paths for the states, the actions, and rewards.
                self.statePath.append(currentState.name)
                self.actionPath.append(randAction)
                self.rewardPath.append(actionRewards[pathIndex])

                # Get the next state from the given action.
                currentState = self.mdpStates[currentState.getActionNextStates(randAction)[pathIndex]] 

            for stateName in self.statePath:
                self.updateStateValue(self.mdpStates.get(stateName))

            self.episodeRewards.append(self.totalReward)
            
            # Print out what happened in that episode.
            self.printEpisode(i)
            self.statePath = []
            self.actionPath = []
            self.rewardPath = []

            self.totalReward = 0

        self.printStatesValues()
        self.printAverageReward()
       

    def pickRandAction(self, state):
        return random.choice(list(state.actions))

    
    def updateStateValue(self, state):
        state.value = state.value + self.alpha * (self.totalReward - state.value)


    def printStatesValues(self):
        for state in self.mdpStates.keys():
            print(state + ": " + str(self.mdpStates.get(state).value))
    
    def printAverageReward(self):
        sum = 0
        for reward in self.episodeRewards:
            sum += reward
        sum = sum / len(self.episodeRewards)
        print("Average Episode Reward: " + str(sum))

    def printEpisode(self, i):
        
        print("____Epidsode " + str(i) + "____")
        # print("State: " + currentState.name + "    Value: " + str(currentState.value))
        print("State Path: " + str(self.statePath))
        print("Action Path: " + str(self.actionPath))
        print("Reward Path: " + str(self.rewardPath))
        print("Total Reward: " + str(self.totalReward))


        
