from glob import glob
import numpy as np
import itertools as it
import data
from data import KeyGroup, LetterGroup, MIN_CYCLE_NUM

global min_w, min_f
min_f = data.f_init

''' 
    文件I/O操作
'''
def GetMatrix(file_path):
    fp = open(file_path, "r")
    return eval(fp.read())

def OutputMatrix(file_path, M):
    fp = open(file_path, "w")
    fp.write(str(M))
    fp.close()

def GenMatrixS(R, f):
    '''
    通过拼音衔接矩阵R和映射f计算键位衔接矩阵S

        Parameters
        ----------
            R   拼音衔接矩阵\n
            f   按键-拼音映射\n
        Returns
        ----------
            S   衔接矩阵\n
'''
    S = np.zeros([26, 26], dtype=float)
    for i in range(0, 26):
        for j in range(0, 26):
            S[i][j] = R[f[i]][f[j]]
    return S

def GetComfort(P, R, f):
    '''
        计算舒适度损失值

        Parameters
        ----------
            P   线段舒适度损失矩阵\n
            R   拼音衔接矩阵\n
            f   按键-拼音映射\n
        Returns
        ----------
            w   舒适度损失值\n
    '''
    S = GenMatrixS(R, f)
    return np.vdot(P, S)

def Traversing(P, R):
    '''
        每次循环中的遍历过程

        Parameters
        ----------
            P   线段舒适度损失矩阵\n
            R   拼音衔接矩阵\n
        Returns
        ----------
            min_f   本次循环中最小损失值对应的映射\n
            min_w   本次循环中的最小损失值\n
    '''
    global min_f, min_w

    min_w = GetComfort(P, R, min_f)
    print("\t{}\t{}\t{}".format(-1, min_w, min_f))

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
            if w/temp <= 0.98:
                break

        print("\t{}\t{}\t{}".format(i, min_w, min_f))

    return min_w, min_f


def JudgeOpt(list_w):
    '''
        判定循环是否继续进行

        Parameters
        ----------
            list_w  记录了之前每次循环的最小损失值数组\n
        Returns
        ----------
            Bool    True则继续优化 否则停止\n
    '''    
    if len(list_w) < MIN_CYCLE_NUM:
        return True

    if list_w[-2] - list_w[-1] > 100:
        return True

    return False

def Replace(P, R):
    '''
        一次循环中对可替换对的选取过程

        Parameters
        ----------
            P   线段舒适度损失矩阵\n
            R   拼音衔接矩阵\n
        Returns
        ----------
            None
    '''    
    global min_f, min_w
    min_w = GetComfort(P, R, min_f)
    print("\t{}\t{}\t{}".format(-1, min_w, min_f))

    for k in range(0,20):
        temp = min_w
        temp_f = min_f
        for i in range(0, 26):
            for j in range(0, 26): #遍历所有可交换对，寻找使w最小的交换对并执行交换
                if ((i == 7) & (j == 25)) | ((j == 7) & (i == 25)): #v和p因为排布问题不交换
                    continue
                else:
                    f = min_f[:]
                    f[i] = min_f[j]
                    f[j] = min_f[i]
                    w = GetComfort(P, R, f)
                    if w < temp:
                        temp = w
                        temp_f = f[:] 
        min_f = temp_f
        min_w = temp
        print("\t{}\t{}\t{}".format(k, temp, temp_f))
                
