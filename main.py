
# coding: utf-8

# In[29]:

import numpy as np


# In[30]:

################
###  CONFIG  ###

# read input file
f = open('input.txt', 'r')

# first line: number of states
n_states = int(f.readline())

# second line: ok states
ok_states = list(map(int, f.readline().split()))

################


# In[31]:

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


# In[32]:

# START Transitions

# read line by line
for line in f:
    if line != '\n':
        t_info = line.split()
        # parse transition info
        add_transition(int(t_info[0]), int(t_info[1]), float(t_info[2]))

# END Transitions


# In[33]:

# compute and get overall result

add_stall()

probs = get_probs()

get_status(probs)
