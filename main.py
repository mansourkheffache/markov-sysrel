
# coding: utf-8

# In[2]:

import numpy as np


# In[82]:

################ 
###  CONFIG  ###

# number of states
n_states = 9

# ok states
ok_states = [0, 1, 2, 3, 5]

################    


# In[ ]:

# magic?

# square transition matrix
t_matrix = np.zeros((n_states, n_states))

# transition definition function
def add_transition(si, sn, p):
    t_matrix[si][sn] = p

# self-transitions
def add_stall():
    s = np.sum(t_matrix, axis=1)
    for i in range(n_states):
        t_matrix[i][i] = 1 - s[i]
        
# compute probabilities
def get_probs():
    # 1. trasnpose
    # 2. subtract Pi
    # 3. add a row of P's
    matrix = np.append((t_matrix.T - np.identity(n_states))[:-1], [np.ones(n_states)], axis=0)
    
    # targets
    t = np.zeros(n_states)
    t[-1] = 1
    
    # solve
    probs = np.linalg.solve(matrix, t)
    
    return probs

# compute network overall reliability
def get_status(probs):
    print(probs)
    prob_good = np.sum(probs[ok_states])
    prob_bad = 1 - prob_good
    
    print("\nOK:" , prob_good)


# In[83]:

# START Transitions

add_transition(0, 1, 0.4)
add_transition(0, 2, 0.4)

add_transition(1, 0, 0.3)
add_transition(1, 3, 0.2)
add_transition(1, 4, 0.4)

add_transition(2, 0, 0.3)
add_transition(2, 4, 0.4)
add_transition(2, 5, 0.2)

add_transition(3, 1, 0.6)
add_transition(3, 6, 0.4)

add_transition(4, 1, 0.3)
add_transition(4, 2, 0.3)
add_transition(4, 6, 0.2)
add_transition(4, 7, 0.2)

add_transition(5, 2, 0.6)
add_transition(5, 7, 0.4)

add_transition(6, 3, 0.3)
add_transition(6, 4, 0.6)
add_transition(6, 8, 0.2)

add_transition(7, 5, 0.3)
add_transition(7, 4, 0.6)
add_transition(7, 8, 0.2)

add_transition(8, 6, 0.6)
add_transition(8, 7, 0.6)

# END Transitions


# In[ ]:

# compute and get overall result

add_stall()

probs = get_probs()

get_status(probs)

