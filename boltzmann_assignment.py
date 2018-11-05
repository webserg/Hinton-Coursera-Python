import numpy as np


# The Boltzmann Machine shown below has two visible units V1V_1V1​ and V2V_2V2​, and one hidden unit hhh.
# Let W1=3W_1=3W1​=3, W2=−1W_2=-1W2​=−1, and bh=−2b_h=-2bh​=−2.
# What is P(V1=1,V2=0)?P(V_1=1, V_2=0)?P(V1​=1,V2​=0)? Write your answer with at least three digits after the decimal point.

def logistic(input):
    return 1 / (1 + np.exp(input))


V = [[[1, 1], [1, 1]], [[1, 0], [1, 0]], [[0, 1], [0, 1]], [[0, 0], [0, 0]]]
h = [1, 0]
W = [3, -1]
bh = -2
minus_energy = np.zeros((4, 2))
for idx_v, v in enumerate(V):
    for idx_vi, vi in enumerate(v):
        for idx_hv, hv in enumerate(h):
            minus_energy[idx_v][idx_hv] = V[idx_v][idx_vi][0] * W[0] * h[idx_hv] + V[idx_v][idx_vi][1] * W[1] * h[
                idx_hv] + bh * h[idx_hv]

print(minus_energy)
# minus_energy = [[0, 2], [1, 3], [-3, -1], [-2, 0]]
# minus_energy = [[2, 2, 1, 0], [1, 2, 0, 0], [0, 0, 1, 0], [-1, 0, 0, 0]]
s = 0
for batch in minus_energy:
    for delta in batch:
        s = s + np.exp(delta)
for batch in minus_energy:
    pv = 0
    for delta in batch:
        pv = pv + np.exp(delta) / s
    print(batch)
    print("pv=" + str(pv))
