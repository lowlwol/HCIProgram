import numpy as np

MIN_CYCLE_NUM = 100

f_init = [14, 22, 17, 12, 20, 24, 18, 5, 4, 3, 7, 2, 25, 8, 9, 16, 23, 0, 6, 10, 13, 11, 15, 19, 1, 21] 

# KeyGroup divides keys into 5 groups and record their indexes
# LetterGroup shows the letters in each groups
KeyGroup = [    [ 0,  4,  8, 13, 17], 
                [10, 16, 20, 21,  9,  5,  6, 12, 14, 18, 24], 
                [ 1, 23,  2,  3,  7, 11, 15, 19, 22, 25]]
LetterGroup = [ [ 8,  0,  4, 14, 20], 
                [ 13, 7,  6,  3, 25, 24, 18, 9, 23, 11,  1], 
                [ 2, 19, 22, 12, 17, 16,  5, 10, 15, 21]]