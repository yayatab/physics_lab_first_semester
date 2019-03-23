import math
from math import sqrt
from constants import *


# todo calss of : name = a +- b with funcitons for a and b.

def calc_Standard_deviation(ls):
    """
    cakcs Standard deviation of ls.
    :param ls:
    :type ls: list
    :return:
    """

    n = len(ls) * 1.0
    s = 0
    avg = sum(ls) / n
    for x in ls:
        s += (x - avg) ** 2

    print("n is   ", n)
    print("avg is ", avg)
    print("sum is", s)
    return avg, math.sqrt(s / (n - 1))


def calc_square(avg_w, avg_l, dw, dl):
    print("@@@@@@@@@@@@@@")
    print(avg_w * avg_l)
    l_deviation = avg_w * dl
    w_deviation = avg_l * dw
    return sqrt(l_deviation ** 2 * w_deviation ** 2)


def n_sigma_str(x1, dx1, ydy_str):
    """

    :param x1:
    :param dx1:
    :param ydy_str:
    :type str:
    :return:
    """
    ydy_str.replace(' ', '')
    x2, dx2 = tuple([float(x) for x in ydy_str.split('±')])
    return n_sigma(x1, dx1, x2, dx2)


def n_sigma_str_str(xdx: str, ydy: str):
    ydy = ydy.replace(' ', '')
    xdx = xdx.replace(' ', '')
    x, dx = tuple([float(a) for a in xdx.split('±')])
    y, dy = tuple([float(a) for a in ydy.split('±')])
    return n_sigma(x, dx, y, dy)


def n_sigma(x1, dx1, x2, dx2):
    counter = abs(x1 - x2)
    denominator = sqrt(dx1 ** 2 + dx2 ** 2)
    return counter / denominator


if __name__ == '__main__':
    w = calc_Standard_deviation([122.0, 121.9, 122.4, 123.3, 122.1])
    print(" @@@@ ")
    l = calc_Standard_deviation([23.7, 26.1, 22.3, 23.7, 25.5, 24.5])
    print(l[1])
    print(calc_square(w[1], l[1], w[0], l[0]))


def get_g(a1):
    return (4 * math.pi ** 2) / a1


def get_Io(a1, m, g, l):
    return a1 * m * g * l / 4 * math.pi ** 2


"""
(4 π^2 I_0)/mgl

"""


def hui(m_tot, dm, i0, di0):
    d1 = 1 / (2 * sqrt(m_tot * i0))
    d1 *= di0

    d2 = (sqrt(i0) / (2 * m_tot * sqrt(m_tot)))
    d2 *= dm

    return sqrt((d1 ** 2 + d2 ** 2))


def get_fall_time_of_ball(L, n, pb, pl, r, g=G_THEO_CM):
    return (9 * L * n) / (2 * g * (pb - pl) * r ** 2)


def get_n(L, t, pb, pl, r, g=G_THEO_CM):
    return (2 * g * (pb - pl) * r ** 2 * t) / (9 * L)


def get_tzmigut(a1, pb, pl, L, g=G_THEO_CM):
    dividee = a1 * 2 * g * (pb - pl)
    divider = 9 * L
    return dividee / divider


def get_tzmigut(a1, pb, pl, L, g=G_THEO_CM):
    dividee = a1 * 2 * g * (pb - pl)
    divider = 9 * L
    return dividee / divider


def visocity(t, pb, pl, L, r, g=G_THEO_CM):
    dividee = t * 2 * g * (pb - pl) * r ** 2
    divider = 9 * L
    return dividee / divider


def delta_eta(a1, da1, pb, dpb, pl, dpl, l, dl, g=G_THEO_CM, dg=G_THEO_CM_D):
    l9 = 9 * l
    vs = [
        (2 * g * (pb - pl) / l9) * da1,
        ((2 * a1 * (pb - pl)) / l9) * dg,
        (2 * g * a1 / l9) * dpb,
        (2 * g * a1 / l9) * dpl,
        (2 * a1 * g * (pb - pl) / (l9 * l)) * dl
    ]
    return sqrt(sum([v ** 2 for v in vs]))


def delta_eta_with_t(t, dt, pb, dpb, pl, dpl, l, dl, g=G_THEO_CM, dg=G_THEO_CM_D):
    l9 = 9 * l
    vs = [
        (2 * g * (pb - pl) / l9) * dt,
        ((2 * t * (pb - pl)) / l9) * dg,
        (2 * g * t / l9) * dpb,
        (2 * g * t / l9) * dpl,
        (2 * t * g * (pb - pl) / (l9 * l)) * dl
    ]
    return sqrt(sum([v ** 2 for v in vs]))


def generic_diviation(s):
    l = [float(x) for x in s.split(' ± ')]
    return l[1] / l[0] * 100
