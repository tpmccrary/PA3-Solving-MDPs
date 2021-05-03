from typing import Dict, List
from pa3_solving_mdps.mdp_state import MDPState
import random

class ValueIteration:

    def __init__(self, mdpStates: Dict[str, MDPState]) -> None:

        self.mdpStates: Dict[str, MDPState] = mdpStates
        self.alpha: float = 0.1
    
    def valueIterationAlg(self) -> None:
        '''
        Value Iteration Algorithm
        '''

        discount = .99

        #Set all value estimates to 0 initially
        V = {}
        for state in self.mdpStates:
            V[state] = 0.

        iterations = 0

        #Continues until convergence is hit, 0.001
        while True:

            
            # Hashtable to hold new values of each state
            newV = {}

            for s in self.mdpStates:
            
                currentState: MDPState = self.mdpStates.get(s)

                # If at the end state
                if (currentState.name == "11aCB"):
                    newV[s] = 0.

                else:

                    print("Previous Value of State: " ,s , ":" ,V[s])

                    maxQValue = -100
                    actionName = ""
                    
                    # Calculate the q value for each available action in the state
                    for action in currentState.actions:
                         
                        qValue = 0

                        # If there are two transitional probablities for a state, it calculates both. 
                        if len(currentState.getActionTransProb(action)) > 1:
                            transProb = currentState.getActionTransProb(action)[1]
                            reward = currentState.getActionRewards(action)[1]
                            state = currentState.getActionNextStates(action)[1]
                            qValue = (transProb*(reward + discount*V[state]))

                        transProb = currentState.getActionTransProb(action)[0]
                        reward = currentState.getActionRewards(action)[0]
                        state = currentState.getActionNextStates(action)[0]
    
                        qValue += (transProb*(reward + discount*V[state]))
                        print("Esitmated Value of Action ", action,": ", qValue)
                        if (maxQValue < qValue):
                            maxQValue = qValue
                            actionName = action
                            
                    newV[s] = maxQValue
                    print("Action Chosen: ", actionName)
                    print("New  Value of State: " , s , ":"  , newV[s])
                    print()

            iterations += 1
            
            #Check for convergence 
            if max(abs(V[state]-newV[state]) for state in self.mdpStates) < .001:
                print("Number of iterations: " , iterations)
                print("CONVERGENCE HIT")

                break

            V = newV
        
        print("Final Values: ", newV)



            
        
# Work of: Timothy P. McCrary, Jesus M. Hernandez