import math
import numpy as np
from math import sqrt
# from constants import *
from constants import G_THEO_CM, G_THEO_CM_D


def _extract_values_from_string(string):
    string.replace(' ', '')
    return tuple([float(x) for x in string.split('±')])


# todo calss add : __add__, __mult__, __div__ etc..
# todo add to class n_sigma calc with another fitobject

class FitObject(object):
    def __init__(self, *args, **kwargs):
        self.val = None
        self.err = None
        if len(args) == 0 and len(kwargs) == 0 and len(args) == 0:
            raise IOError("WAT? insert a string, or val=XXX, err=XXX")
        elif len(args) == 1:
            self.val, self.err = _extract_values_from_string(args[0])
        elif len(args) == 2:
            self.val = float(args[0])
            self.err = float(args[1])
        elif self.val is None or self.err is None:
            self.val = kwargs['val']
            self.err = kwargs['err']
        if self.val is None or self.err is None:
            raise IOError("WAT?\ninsert a string OR\nval=XXX, err=XXX OR\n<val>,<err>")

    def stat_err(self):
        return self.err / self.val

    def __repr__(self):
        return "{a} ± {b}, {c}".format(a=self.val, b=self.err, c=self.stat_err())
    
    def __add__(self, other):
        return self.val + other.val, sqrt(self.err + other.err)

    def __sub__(self, other):
        return self.val - other.val, sqrt(self.err + other.err)


def randomize_a(init, n):
    rand = np.random.randint(10, size=n)
    return [init ** x for x in rand]


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
    dx2, x2 = _extract_values_from_string(ydy_str)
    return n_sigma(x1, dx1, x2, dx2)


def n_sigma_str_str(xdx: str, ydy: str):
    x, dx = _extract_values_from_string(xdx)
    y, dy = _extract_values_from_string(ydy)
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


def calc_sigma_div(*args):
    return sqrt(sum(d ** 2 for d in args))


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
