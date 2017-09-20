# Markov System Reliability
System Reliability modeling using Markov chains, using Numpy


## HOWTO

This script can only be used to simulate the behavior of a system that is already modelled using Markov Chains. It basically transforms the problem into a matrix, and solves linear systems of equations in order to reach a solution - by determining the probability of being at a given state in the system.

The default input file name is `input.txt`, and the format is as follows:

```{r}
FIRSTLINE     - number of states. e.g. "4"
SECONDLINE    - list of 'good' states, seperated by spaces. e.g. "0 1 2 4"

OTHERLINES    - definition of transitions, each on a seperate lines. e.g. "1 2 0.3" (transition from STATE1 to STATE2 with prob = 0.3)

```
Note that you cannot have blank spaces seperating the first two definition lines, but can seperate your transitions by grouping them together using blank lines.


Feel free to edit the script and play around with it.

Happy hacking!
