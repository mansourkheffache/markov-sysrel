import numpy as np

# Refactoring of the used methods to be more suitable for the test cases

class markov_sysrel:
    
    def __init__(self, n_states, ok_states, transitions):
        self.__nStates = n_states
        self.__okStates = ok_states
        self.__transitions = transitions
        
    def add_transition(self, si, sn, p, inputMatrix):
        inputMatrix[si][sn] = p
    
    def add_stall(self, numberOfStates, inputMatrix):
        s = np.sum(inputMatrix, axis=1)
        for i in range(numberOfStates):
            inputMatrix[i][i] = 1 - s[i]
    
    def get_probs(self, inputMatrix, numberOfStates):
        matrix = np.append((inputMatrix.T - np.identity(numberOfStates))[:-1], [np.ones(numberOfStates)], axis=0)
        t = np.zeros(numberOfStates)
        t[-1] = 1
        probs = np.linalg.solve(matrix, t)
        return probs
    
    def get_status(self, probs, okStates):
        prob_good = np.sum(probs[okStates])
        #prob_bad = 1 - prob_good    
        #print("\nOK:" , prob_good)
        return prob_good
    
    def get_probability(self):
        t_matrix = np.zeros((self.__nStates, self.__nStates))
        for transition in self.__transitions:
            self.add_transition(transition[0], transition[1], transition[2], t_matrix)
        self.add_stall(self.__nStates, t_matrix)
        probs = self.get_probs(t_matrix, self.__nStates)
        return self.get_status(probs, self.__okStates)  
