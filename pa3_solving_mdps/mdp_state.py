
class MDPState:

    name = None
    # Hashtable
    actions = {}


    def __init__(self, name) -> None:
        self.name = name

    def addAction(self, action, rewards, nextStates, transProbs=[1]):
        self.actions[action] = [rewards, nextStates, transProbs]

    def getActionRewards(self, action):
        return self.actions.get(action)[0]

    def getActionNextStates(self, action):
        return self.actions.get(action)[1]

    def getActionTransProb(self, action):
        return self.actions.get(action)[2]
