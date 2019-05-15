from math import sqrt

from general_tools.electricity import MEUE_ZERO
from general_tools.lab import calc_sigma_div


def print_header():
    print("@" * 80)
    print("@" * 80)
    print("@" * 80)


def calc_l_d(a2, da2, L, dL, l, dl):
    val = (2 * a2) / (L + l / 2)
    d1 = (2 * da2) / (L + l / 2)
    d3 = (2 * a2 * dL) / (L + l / 2) ** 2
    d4 = (a2 * dl) / (2 * (L + l / 2) ** 2)
    return val, calc_sigma_div(d1, d3, d4)


def kkk(a2, da2, L, dL, n, dn):
    val = (2 * a2) / (L + dn / 2)

    deriv = n * MEUE_ZERO * L ** 2
    d1 = (2 * sqrt(2) * da2 * a2) / deriv ** 2
    d2 = (4 * sqrt(2) * dL * a2 ** 2) / (L * deriv ** 2)
    d3 = (2 * sqrt(2) * dn) / (n * deriv ** 2)
    return val, calc_sigma_div(d1, d2, d3)


def theo_ld(l, d, dl=0.00733234842, dd=0.00733234842):
    return l / d, calc_sigma_div(dl / d, ((l * dd) / d ** 2))


def e_me(a2, da2, L, dL, n, dn):
    val = a2 * 2 * sqrt(2)
    deriv = n * MEUE_ZERO * L ** 2
    val = val / deriv

    d1 = (16 * da2 * a2) / deriv ** 2
    d2 = (32 * dL * a2 ** 2) / (L * deriv ** 2)
    d3 = (16 * a2 ** 2 * dn) / (n * deriv ** 2)
    return val, sum(x ** 2 for x in [d1, d2, d3])
