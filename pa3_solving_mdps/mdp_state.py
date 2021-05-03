from __future__ import annotations
from typing import Dict, List
import random

class MDPState: 
    '''Object class that represents a state in the MDP.
    '''

    def __init__(self, name: str) -> None:
        '''Given a state name, assigns it to thi sobject.

        Args:
            name (str): The name of the state.
        '''
        # The name of the state (i.e. RU8p)
        self.name: str = name
        # The actions of the sate represented as a hash table (i.e. actions = {"P": [], "R": []]})
        self.actions: Dict[str, List] = {}
        # The value of this state.
        self.value: int = 0

    def addAction(self, action: str, rewards: List[int], nextStates: List[str], transProbs: List[int], qValue: List[float]) -> None:
        '''This function adds an action to the state given the actions: rewards, next states, and transitional probability.

        Args:
            action (str): The action to add to the state.
            rewards (List[int]): The list of rewards for taking action.
            nextStates (List[str]): The list of states for taking action.
            transProbs (List[int], optional): The list of transitional probabilities for taking action. Defaults to [1].
            qValue (List[int], optional): The list of qvalues for taking action. Defaults to [0].
        '''
        
        self.actions[action] = [rewards, nextStates, transProbs, qValue]

    
    def getActionRewards(self, action: str) -> List[int]:
        '''Given an action, returns the list of rewards for taking that action.

        Args:
            action (str): The action to take.

        Returns:
            List[int]: The list of rewards.
        '''

        return self.actions.get(action)[0]

    def getActionNextStates(self, action: str) -> List[str]:
        '''Given an action, returns the list next states for taking that action

        Args:
            action (str): The action to take.

        Returns:
            List[str]: The list of next states.
        '''
        
        return self.actions.get(action)[1]

    def getActionTransProb(self, action: str) -> List[str]:
        '''Given an action, returns the list of transitional probabilities for that action.

        Args:
            action (str): The action to take.

        Returns:
            List[str]: The list of transitional probabilites.
        '''
        return self.actions.get(action)[2]

    def getActionQValues(self, action: str) -> List[float]:
        return self.actions.get(action)[3]

    def setActionQValue(self, action: str, qValue: float, index: int) -> None:
        self.actions.get(action)[3][index] = qValue

    @staticmethod
    def pickRandAction(state: MDPState) -> str:
        '''Given a state, returns a random action from that state.

        Args:
            state (MDPState): The state.

        Returns:
            str: A random action from state.
        '''
        return random.choice(list(state.actions))

    @staticmethod
    def getBestQValueAction(state: MDPState) -> str:
        actions: List[str] = list(state.actions.keys())
        qValues: List[float] = []

        for action in actions:
            qValues.append(state.getActionQValues(action)[0])

        maxQValue: float = max(qValues) 
        index: int = qValues.index(maxQValue)

        return actions[index]        

        


# Work of: Timothy P. McCrary, Jesus M. Hernandez

