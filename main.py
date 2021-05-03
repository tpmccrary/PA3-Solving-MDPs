from typing import Dict
from pa3_solving_mdps.monte_carlo import MonteCarlo
from pa3_solving_mdps.value_iteration import ValueIteration
from pa3_solving_mdps.q_learning import QLearning
from pa3_solving_mdps.mdp_state import MDPState
import sys

def main():
    '''Main method for this project.
    '''
    # Check to make sure the right ammount of commands are inputed.
    if (len(sys.argv) != 2):
        print("Incorrect commands: Example command: 'python3 main.py 1'")
        sys.exit(1)

    # Get the algorithm choice from the arguments
    algoChoice: int = int(sys.argv[1])

    # Model the MDP.
    mdpStates = modelMDP()


    # valueIteration = ValueIteration()
    
    if (algoChoice == 1):
        monteCarlo = MonteCarlo(mdpStates)
        monteCarlo.monteCarloAlg()
    elif (algoChoice == 2):
        pass
    elif (algoChoice == 3):
        qLearning = QLearning(mdpStates)
        qLearning.qLearningAlg("RU8p", "11aCB")
    else:
        print("Not a valid command, please use 1, 2, or 3.")
        sys.exit(0)

def modelMDP() -> Dict[str, MDPState]:
    '''Returns a modeled MDP as a dictionary with MDPState objects.

    Returns:
        Dict[str, MDPState]: The modeled MDP as a dictionary.
    '''
    # START: Model of the MDP.
    mdpStates = {}

    # Adding state RU8p, along with its actions.
    mdpState = MDPState("RU8p")
    mdpState.addAction("P", [2], ["TU10p"], [1], [0.0])
    mdpState.addAction("R", [0], ["RU10p"], [1], [0.0])
    mdpState.addAction("S", [-1], ["RD10p"], [1], [0.0])
    mdpStates[mdpState.name] = mdpState

    mdpState = MDPState("TU10p")
    mdpState.addAction("P", [2], ["RU10a"], [1], [0.0])
    mdpState.addAction("R", [0], ["RU8a"], [1], [0.0])
    mdpStates[mdpState.name] = mdpState

    mdpState = MDPState("RU10p")
    mdpState.addAction("R", [0], ["RU8a"], [1], [0.0])
    mdpState.addAction("P", [2, 2], ["RU8a", "RU10a"], [.5, .5], [0.0])
    mdpState.addAction("S", [-1], ["RD8a"], [1], [0.0])
    mdpStates[mdpState.name] = mdpState

    mdpState = MDPState("RD10p")
    mdpState.addAction("R", [0], ["RD8a"], [1], [0.0])
    mdpState.addAction("P", [2, 2], ["RD8a", "RD10a"], [.5, .5], [0.0])
    mdpStates[mdpState.name] = mdpState

    mdpState = MDPState("RU8a")
    mdpState.addAction("P", [2], ["TU10a"], [1], [0.0])
    mdpState.addAction("R", [0], ["RU10a"], [1], [0.0])
    mdpState.addAction("S", [-1], ["RD10a"], [1], [0.0])
    mdpStates[mdpState.name] = mdpState

    mdpState = MDPState("RD8a")
    mdpState.addAction("R", [0], ["RD10a"], [1], [0.0])
    mdpState.addAction("P", [2], ["TD10a"], [1], [0.0])
    mdpStates[mdpState.name] = mdpState

    mdpState = MDPState("TU10a")
    mdpState.addAction("any", [-1], ["11aCB"], [1], [0.0])
    mdpStates[mdpState.name] = mdpState

    mdpState = MDPState("RU10a")
    mdpState.addAction("any", [0], ["11aCB"], [1], [0.0])
    mdpStates[mdpState.name] = mdpState

    mdpState = MDPState("RD10a")
    mdpState.addAction("any", [4], ["11aCB"], [1], [0.0])
    mdpStates[mdpState.name] = mdpState

    mdpState = MDPState("TD10a")
    mdpState.addAction("any", [3], ["11aCB"], [1], [0.0])
    mdpStates[mdpState.name] = mdpState

    mdpState = MDPState("11aCB")
    mdpStates[mdpState.name] = mdpState

    return mdpStates


if __name__ == '__main__':
    main()

# Work of: Timothy P. McCrary, Jesus M. Hernandez
