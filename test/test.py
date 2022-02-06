# fpi = open("Matrix_R.txt", "r")
# fpo = open("Matrix_C.txt", "w")
# C = eval(fpi.read())
# print(type(C))

import numpy as np

a = [[3, 4], [5, 6]]
b = [[1, 2], [7, 8]]
print(np.vdot(a, b))

