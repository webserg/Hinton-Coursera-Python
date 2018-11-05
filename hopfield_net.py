import random

import numpy as np


# http://web.cs.ucla.edu/~rosen/161/notes/hopfield.html
class Hopfield_net(object):
    weights = []
    n = 0

    def __init__(self, n):
        self.weights = np.zeros((n, n), dtype=int)
        self.n = n

    def train(self, v):
        i = 0
        j = i + 1
        n = self.n
        w = np.zeros((n, n), dtype=int)
        while i < n - 1:
            while j < n:
                w[i, j] = (2 * v[i] - 1) * (2 * v[j] - 1)
                j = j + 1
            i = i + 1
            j = i + 1
        return w + w.T

    def save(self, w):
        self.weights = self.weights + w
        return self.weights

    def update_node(self, i, v):
        node = np.dot(self.weights[i], v)
        return node

    def update_vector(self, v):
        k = 0
        not_updating = 0
        while k < 5:
            while not_updating < self.n:
                nodes_nums = [x for x in range(self.n)]
                random.shuffle(nodes_nums)
                print(nodes_nums)
                not_updating = 0
                for num in nodes_nums:
                    res = self.update_node(num, v)
                    if res >= 0:
                        if v[num] != 1:
                            v[num] = 1
                        else:
                            not_updating = not_updating + 1
                    else:
                        if v[num] != 0:
                            v[num] = 0
                        else:
                            not_updating = not_updating + 1
                print(v)
            k = k + 1
            not_updating = 0
        return v


def main():
    n = 5
    net = Hopfield_net(n)
    v = np.array([0, 1, 1, 0, 1])
    # net.train(v)
    i = 0
    j = i + 1
    w = np.zeros((n, n), dtype=int)
    while i < n - 1:
        while j < n:
            w[i, j] = (2 * v[i] - 1) * (2 * v[j] - 1)
            j = j + 1
        i = i + 1
        j = i + 1
    print(w + w.T)
    nums = [x for x in range(10)]
    random.shuffle(nums)
    print(nums)


def main_train():
    n = 5
    net = Hopfield_net(n)
    v = np.array([0, 1, 1, 0, 1])
    w = net.train(v)
    print(w)
    net.save(w)
    v2 = np.array([1, 0, 1, 0, 1])
    w2 = net.train(v2)
    print(w2)
    saved = net.save(w2)
    print(saved)
    v3 = np.array([1, 1, 1, 1, 1])
    # print(net.update_node(2, v3))
    print(net.update_vector(np.array([1, 0, 1, 1, 1])))


if __name__ == "__main__":
    main_train()

