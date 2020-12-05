import numpy as np


def recalcXC(xtab):
    xctab = np.zeros((2, 2))

    len_zero = 0
    len_one = 0

    for i in xtab:
        if i[2] == 0:
            len_zero += 1
            xctab[0][0] += i[0]
            xctab[0][1] += i[1]
        else:
            len_one += 1
            xctab[1][0] += i[0]
            xctab[1][1] += i[1]

    xctab[0][0] /= len_zero
    xctab[0][1] /= len_zero
    xctab[1][0] /= len_one
    xctab[1][1] /= len_one

    return xctab
