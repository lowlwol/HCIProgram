import numpy as np

fpi = open("Matrix_C.txt", "r")
fpo = open("Matrix_D.txt", "w")
C = eval(fpi.read())
D = [[0 for i in range(0, 8)] for j in range(0, 16)]

for i in range(0, 16):
    for j in range(0, 8):
        D[i][j] = 100 - C[i][j]

fpo.write(str(D))

fpo.close()
fpi.close()
