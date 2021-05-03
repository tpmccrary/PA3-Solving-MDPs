from typing import Dict
from pa3_solving_mdps.monte_carlo import MonteCarlo
from pa3_solving_mdps.value_iteration import ValueIteration
from pa3_solving_mdps.q_learning import QLearning
from pa3_solving_mdps.mdp_state import MDPState

def main():
    '''Main method for this project.
    '''

    mdpStates = modelMDP()


    # monteCarlo = MonteCarlo(mdpStates)
    # monteCarlo.monteCarloAlg()

    valueIteration = ValueIteration(mdpStates)
    valueIteration.valueIterationAlg()
    

    # qLearning = QLearning()

def modelMDP() -> Dict[str, MDPState]:
    '''Returns a modeled MDP as a dictionary with MDPState objects.

    Returns:
        Dict[str, MDPState]: The modeled MDP as a dictionary.
    '''
    # START: Model of the MDP.
    mdpStates = {}

    # Adding state RU8p, along with its actions.
    mdpState = MDPState("RU8p")
    mdpState.addAction("P", [2], ["TU10p"])
    mdpState.addAction("R", [0], ["RU10p"])
    mdpState.addAction("S", [-1], ["RD10p"])
    mdpStates[mdpState.name] = mdpState

    mdpState = MDPState("TU10p")
    mdpState.addAction("P", [2], ["RU10a"])
    mdpState.addAction("R", [0], ["RU8a"])
    mdpStates[mdpState.name] = mdpState

    mdpState = MDPState("RU10p")
    mdpState.addAction("R", [0], ["RU8a"])
    mdpState.addAction("P", [2, 2], ["RU8a", "RU10a"], [.5, .5])
    mdpState.addAction("S", [-1], ["RD8a"])
    mdpStates[mdpState.name] = mdpState

    mdpState = MDPState("RD10p")
    mdpState.addAction("R", [0], ["RD8a"])
    mdpState.addAction("P", [2, 2], ["RD8a", "RD10a"], [.5, .5])
    mdpStates[mdpState.name] = mdpState

    mdpState = MDPState("RU8a")
    mdpState.addAction("P", [2], ["TU10a"])
    mdpState.addAction("R", [0], ["RU10a"])
    mdpState.addAction("S", [-1], ["RD10a"])
    mdpStates[mdpState.name] = mdpState

    mdpState = MDPState("RD8a")
    mdpState.addAction("R", [0], ["RD10a"])
    mdpState.addAction("P", [2], ["TD10a"])
    mdpStates[mdpState.name] = mdpState

    mdpState = MDPState("TU10a")
    mdpState.addAction("any", [-1], ["11aCB"])
    mdpStates[mdpState.name] = mdpState

    mdpState = MDPState("RU10a")
    mdpState.addAction("any", [0], ["11aCB"])
    mdpStates[mdpState.name] = mdpState

    mdpState = MDPState("RD10a")
    mdpState.addAction("any", [4], ["11aCB"])
    mdpStates[mdpState.name] = mdpState

    mdpState = MDPState("TD10a")
    mdpState.addAction("any", [3], ["11aCB"])
    mdpStates[mdpState.name] = mdpState

    mdpState = MDPState("11aCB")
    mdpStates[mdpState.name] = mdpState

    return mdpStates


if __name__ == '__main__':
    main()

# Work of: Timothy P. McCrary, Jesus M. Hernandez
