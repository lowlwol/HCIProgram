# block size
height = float(1.15)
width  = float(1)

# line lists of row and col
l_r = []
l_c = []
for i in range(0, 17):
    l_r.append(height * i)
for i in range(0, 9 ):
    l_c.append(width  * i)

# position of keys (index)
key = [[5, 4], [5, 5], [5, 6], [6, 3], [6, 4], [6, 5], [6, 6], [6, 7],
        [7, 4], [7, 5], [7, 6], [7, 7], [8, 4], [8, 5], [8, 6], [8, 7],
        [9, 4], [9, 5], [9, 6], [9, 7], [10, 5], [10, 6], [10, 7], 
        [11, 5], [11, 6], [11, 7]]

# target matrix L
L = [   
        [   
            [   
                [
                    0 for i in range(0, 8)
                ] for i in range(0, 16)
            ] for i in range(0, 26)
        ] for i in range(0, 26)
    ]