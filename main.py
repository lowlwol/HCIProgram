# -*- coding:utf-8 -*-

import numpy as np
import func
import data

#遍历分组优化

if __name__ == "__main__":
    # 创建输出文件
    fpo = open("Output.txt", "w")
    # 读取事先计算好的线段舒适度损失矩阵P和拼音衔接频次矩阵R
    P = func.GetMatrix("Matrix_P.txt")
    R = func.GetMatrix("Matrix_R.txt")

    cycle_num = 0           # 记录循环次数
    w_list = []             # 记录每一轮循环的最小损失值

    while func.JudgeOpt(w_list):                # 判定循环是否继续进行
        min_w, min_f = func.Traversing(P, R)    # 遍历过程
        w_list.append(min_w)
        cycle_num += 1
        print("{}\t{}\t{}".format(cycle_num, min_w, min_f))
        fpo.write("No.{}\n{}\n{}\n\n".format(cycle_num, min_f, min_w))

    fpo.close()