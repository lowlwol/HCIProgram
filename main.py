import numpy as np
import func
import data

if __name__ == "__main__":
    fpo = open("Output.txt", "w")
    cycle_num = 0
    min_f = np.zeros(26)
    min_w = float(20000000.)
    while cycle_num < data.MIN_CYCLE_NUM or func.JudgeOpt(min_w):
        min_f, min_w = func.Traversing(fpo)
        cycle_num += 1
        print(cycle_num, min_w)