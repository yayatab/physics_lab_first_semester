from general_tools.lab import *
from general_tools.general_math import *


def generate_phase_shift(A, B):
    return math.asin(B / A)


def phase_from_dt(omega, dt):
    return omega * dt
