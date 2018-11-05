import itertools as it
import random

import numpy as np

# To find an energy minimum in this
# net, start from a random state and
# then update units one at a time in
# random order.
# – Update each unit to whichever
# of its two states gives the
# lowest global energy.
n = 5
V = list(it.product([0, 1], repeat=n))
init_V = random.randint(0, len(V))
W = np.zeros((n, n), dtype=int)
W[0][2] = W[1][2] = 1
W[2][4] = W[2][3] = 2
W[1][4] = -3
W[0][3] = -2
W[3][4] = 3

W = W + W.T
minus_energy = np.zeros((len(V), 1))
nodes_nums = [x for x in range(n)]
random.shuffle(nodes_nums)
print(nodes_nums)
E=[]
for S in V:
    E1 = 0
    x = np.array(S)
    for num in nodes_nums:
        E1 = -1 * (np.dot(np.dot(x, W), x.T) / 2)
        x2 = x
        E2 = -1 * (np.dot(np.dot(x2, W), x2.T) / 2)
        if x2[num] == 0:
            x2[num] = 1
        else:
            x2[num] = 0
        if E2 < E1:
            x = x2
            E.append(E2)
        else:
            E.append(E1)
res = list(set(E))
res.sort()
print(res)
