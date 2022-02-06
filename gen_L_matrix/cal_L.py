from data import height, width, L, l_r, l_c, key
from func import MakeMat


if __name__ == "__main__":
    for i in range(0, 26):
        for j in range(0, 26):
            MakeMat(i, j)

    # output target matrix L to a file
    fp = open("Matrix_L.txt", "w")
    fp.write(str(L))
    fp.close()