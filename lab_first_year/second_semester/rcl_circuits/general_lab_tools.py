from general_tools.lab import *
from general_tools.general_math import *


def generate_phase_shift(A, B):
    return math.asin(B / A)


def phase_from_dt(omega, dt):
    return omega * dt


def vr_vo(R, omega, L, c):
    return R / sqrt(R ** 2 + (omega * L - 1 / (omega * c)))


def get_omega(L, DL, C, DC):
    return 1 / sqrt(L * C), 0.5 * sqrt((DC / L) ** 2 + (DL / C) ** 2)


def get_delta_omega(R, L=23.91e-3):
    return R / L


def print_asins(A, B):
    for r in calc_asin_on_lists(A, B):
        print(r)


def generate_w0_anddelta_w_from_fit(a1, da1, a2, da2):
    w0 = 1 / sqrt(a1 * a2)
    dw0 = 0.5 * sqrt((da1 / a2) ** 2 + (da2 / a1)) ** 2

    deltaw = 1 / a1
    deltadw = da1 / a1
    return (w0, dw0), (deltaw, deltadw)
