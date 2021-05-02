
class MDPState: 

    def __init__(self, name) -> None:
        self.name = name
        self.actions = {}
        self.value = 0

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

