import numpy as np


def estimate_optdx(f, x0):
    dx = [10 ** -i for i in range(1, 15)]

    dfdx = []
    for i in range(len(dx)):
        x = f(x0 + dx[i]) - f(x0)
        x = x / dx[i]
        dfdx.append(x)

    eps = [np.abs(dfdx[i] - dfdx[i - 1]) for i in range(1, len(dfdx))]

    value = dx[0]

    for i in range(1, len(dx)):
        if eps[i - 1] > eps[i]:
            value = dx[i + 1]
        else:
            break

    return value
