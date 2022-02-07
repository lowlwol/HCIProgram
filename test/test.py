import numpy as np
import itertools as it

A = [3, 4, 5]

for item in it.permutations(A, len(A)):
    B = np.reshape(item, 3)
    print(item, B)