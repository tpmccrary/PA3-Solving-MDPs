
# Object that represents a state in the MDP.
class MDPState: 

    def __init__(self, name) -> None:
        # The name of the state (i.e. RU8p)
        self.name = name
        # The actions of the sate represented as a hash table (i.e. actions = {"P": [], "R": []]})
        self.actions = {}
        self.value = 0

    # Adds an action to the state.
    '''
    @param self: This object.
    @param action: An action 
    '''
    def addAction(self, action, rewards, nextStates, transProbs=[1]):
        self.actions[action] = [rewards, nextStates, transProbs]

    def getActionRewards(self, action):
        # First element in actions list, which is rewards.
        # actions = {"P": [[2], ["TU10a"], [1]]}
        return self.actions.get(action)[0]

    def getActionNextStates(self, action):
        return self.actions.get(action)[1]

    def getActionTransProb(self, action):
        return self.actions.get(action)[2]

