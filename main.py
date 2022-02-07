import numpy as np
import func
import data

if __name__ == "__main__":
    fpo = open("Output.txt", "w")
    P = func.GetMatrix("Matrix_P.txt")
    R = func.GetMatrix("Matrix_R.txt")

    cycle_num = 0
    w_list = []             # record min_w

    while cycle_num < data.MIN_CYCLE_NUM or func.JudgeOpt(w_list):
        min_w, min_f = func.Traversing(P, R, fpo)
        cycle_num += 1
        w_list.append(min_w)
        print(cycle_num, min_w)
        fpo.write("No.{}\n{}\n{}\n\n".format(cycle_num, min_f, min_w))

    fpo.close()