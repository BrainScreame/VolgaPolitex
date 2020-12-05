import numpy as np


def estimate_optdx(f, x0):
    dx = [10 ** -i for i in range(1, 15)]

    dfdx = []
    for i in range(len(dx)):
        x = (f(x0 + dx[i]) - f(x0 - dx[i])) / (2 * dx[i])
        dfdx.append(x)

    eps = [np.abs(dfdx[i] - dfdx[i - 1]) for i in range(1, len(dfdx))]

    value = dx[0]

    for i in range(1, len(dx)):
        if eps[i - 1] > eps[i]:
            value = dx[i + 1]
        else:
            break

    return value


def df(f, x0, dx):
    l = f(x0 + dx) - f(x0 - dx)
    return l / (2 * dx)


def estimate_dfdx_error(f, a, b):
    x = np.linspace(a, b, 100)
    x1 = np.empty(len(x))
    max_ot = 0
    em_list = np.array([estimate_optdx(f, a), estimate_optdx(f, b), estimate_optdx(f, (a + b) / 2)])
    em = em_list.mean()

    for i in range(len(x)):
        x1[i] = x[i] * (1 + 1e-14)
        otk = abs(df(f, x[i], em) - df(f, x1[i], em))

        if otk > max_ot:
            max_ot = otk

    return max_ot
