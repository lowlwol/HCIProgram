from glob import glob
import numpy as np
import itertools as it
import data
from data import KeyGroup, LetterGroup, MIN_CYCLE_NUM


global min_w, min_f
min_f = data.f_init
min_w = float(6963200.304931576)


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
    C = GetMatrix("Matrix_D.txt")
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


def GetComfort(P, R, f):
    S = GenMatrixS(R, f)
    return np.vdot(P, S)


'''
    return
        min_f   f of min w in 
        min_w   min w value
'''
def Traversing(P, R):
    global min_f, min_w

    w = GetComfort(P, R, min_f)
    print("\t{}\t{}\t{}".format(-1, w, min_f))

    for i in range(0, 3):
        lenth = len(LetterGroup[i])
        temp = min_w
        f = min_f[:]
        for tItem in it.permutations(LetterGroup[i], lenth):    # traversing in a group
            item = np.reshape(tItem, lenth)                     # trans tuple into tensor
            for j in range(0, lenth):
                f[KeyGroup[i][j]] = item[j]
            w = GetComfort(P, R, f)
            if w < min_w:
                min_w = w
                min_f = f[:]                                    # shallow copy
            if w/temp <= 0.99:
               break

        print("\t{}\t{}\t{}".format(i, min_w, min_f))

    return min_w, min_f


'''
    return
        True    Amount of optimization keeps changing
        False   Amount of optimization changes too slow 
'''
def JudgeOpt(list_w):
    if len(list_w) < MIN_CYCLE_NUM:
        return True

    if list_w[-2] - list_w[-1] > 100:
        return True

    return False
