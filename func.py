import numpy as np
import func

''' 
    file I/O
'''
def GetMatrix(file_path):
    fp = open(file_path, "r")
    return eval(fp.read())

def OutputMatrix(file_path, M):
    fp = open(file_path, "w")
    fp.write(str(M))
    fp.close()


'''
    Major functions
'''
# only runs once to generate matrix p, 
def GenMatrixP():
    L = GetMatrix("Matrix_L.txt")
    C = GetMatrix("Matrix_C.txt")
    P = [[0 for i in range(0, 26)] for j in range(0, 26)]
    for i in range(0,26):
        for j in range(0, 26):
            P[i][j]= np.vdot(L[i][j], C)
    OutputMatrix("Matrix_P.txt", P)

def GenMatrixS(R, f):
    S = np.zeros([26, 26], dtype=float)
    for i in range(0, 26):
        for j in range(0, 26):
            S[i][j] = R[f[i]][f[j]]
    return S

def GetComfort(f):
    P = func.GetMatrix("Matrix_P.txt")
    R = func.GetMatrix("Matrix_R.txt")
    S = func.GenMatrixS(R, f)
    return np.vdot(P, S)