import numpy as np
import func
import data

#对换遍历优化

if __name__ == "__main__":
    # 创建输出文件
    fpo = open("Output.txt", "w")
    # 读取事先计算好的线段舒适度损失矩阵P和拼音衔接频次矩阵R
    P = func.GetMatrix("Matrix_P.txt")
    R = func.GetMatrix("Matrix_R.txt")

    cycle_num = 0           # 记录循环次数
    w_list = []             # 记录每一轮循环的最小损失值

    func.Replace(P, R)      # 替换过程

    fpo.close()