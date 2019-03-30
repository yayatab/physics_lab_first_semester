from general_tools.lab import *
from general_tools.general_math import *


def generate_phase_shift(A, B):
    return math.asin(B / A)


def phase_from_dt(omega, dt):
    return omega * dt


def vr_vo(R, omega, L, c):
    return R / sqrt(R ** 2 + (omega * L - 1 / (omega * c)))


def get_omega(L, C):
    return 1 / sqrt(L * C)


def get_delta_omega(R, L=23.91e-3):
    return R / L


def print_asins(A, B):
    for r in calc_asin_on_lists(A, B):
        print(r)
