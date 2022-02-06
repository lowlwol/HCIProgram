from data import height, width, L, l_r, l_c, key


def swap(a, b):
    return b, a


def cmp_x(p):
    return p[0]


''' 
    coordinates functions
                y
    0 ---------> 
     |
     |
     |
     v
    x
'''
''' get distance between 2 points p1 & p2 '''
def CulDis(p1, p2):
    return pow((p1[0]-p2[0])**2+(p1[1]-p2[1])**2, 0.5)


''' return the area index of point p '''
def LocateArea(p):
    x = -1
    y = -1
    for i in range(0, 16):
        if p[0] > l_r[i] and p[0] < l_r[i+1]:
            x = i
    for j in range(0, 8 ):
        if p[1] > l_c[j] and p[1] < l_c[j+1]:
            y = j
    return x, y


''' 
    make target matrix:
    i, j are the index of keys.
    calculate the lenths in different blocks of 
    the straight path between 2 keys.
'''
def MakeMat(i, j):
    if i == j:
        return
    # index
    ix0 = key[i][0]
    iy0 = key[i][1]
    ix1 = key[j][0]
    iy1 = key[j][1]
    # horizontal lines
    if ix0 == ix1:
        ya = min(iy0, iy1)
        yb = max(iy0, iy1)
        for y in range(ya, yb+1):
            if y == ya or y == yb:
                L[i][j][ix0][y] += width / 2
            else:
                L[i][j][ix0][y] += width
    # vertical lines
    elif iy0 == iy1:
        xa = min(ix0, ix1)
        xb = max(ix0, ix1)
        for x in range(xa, xb+1):
            if x == xa or x == xb:
                L[i][j][x][iy0] += height / 2
            else:
                L[i][j][x][iy0] += height
    # other lines
    else:
        # coordinate
        x0 = float(ix0 + height / 2)
        y0 = float(iy0 + width  / 2)
        x1 = float(ix1 + height / 2)
        y1 = float(iy1 + width  / 2)
        # y = k * x + b
        k = (y1 - y0) / (x1 - x0)
        b = y0 - k * x0

        intersections = [[x0, y0], [x1,y1]]
        for x in l_r:
            if x > x0 and x < x1:
                intersections.append([x, k*x+b])
            if x < x0 and x > x1:
                intersections.append([x, k*x+b])
        for y in l_c:
            if y > y0 and y < y1:
                intersections.append([(y-b)/k, y])
            elif y < y0 and y > y1:
                intersections.append([(y-b)/k, y])

        # the segment in a block consists of 2 adjacent point 
        intersections.sort(key=cmp_x)
        for k in range(0, len(intersections)-1):
            # locate the area of a segment through the midpoint
            p_mid = [(intersections[k][0] + intersections[k+1][0]) / 2, 
                        (intersections[k][1] + intersections[k+1][1]) / 2]
            x, y = LocateArea(p_mid)
            # print(i, j, x, y, p_mid)
            L[i][j][x][y] += CulDis(intersections[k], intersections[k+1])