from general_tools.lab import *

"""
(I_A-I_b)/(1/2 (I_A+I_B ) )
"""


def get_s(d, delta_d):
    return pi * (d / 2) ** 2, pi * d * delta_d


def get_rho(s, ds, a2, da2):
    d1 = s * da2
    d2 = a2 * ds
    return a2 * s, sqrt(d1 ** 2 + d2 ** 2)


def get_diff(xa, xb):
    up = abs(xa - xb)
    down = 0.5 * (xa + xb)
    return up / down


"""
nichrome - 1.12 , 0.05e-06Ω from wiki
s - 4.68E-08, 2.21E-10

"""