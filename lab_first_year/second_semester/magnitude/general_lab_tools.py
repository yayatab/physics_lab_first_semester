from constants import pi
from general_tools.electricity import generate_field_radial_part
from general_tools.lab import n_sigma
from general_tools.general_math import *
from general_tools import plotting, convertions, electricity

R = 13  # in cm
ELECTRIC_FIELD_AT_R = 0.039, 0.00106453  # Mt
OUR_OMEGA = 30

Bearth = (0.039, 3.65E-04)


def degrees_delta():
    return (1 / 180) * math.pi / sqrt(12)


def ruler_delta(resolution_meter=1e-3):
    return resolution_meter / sqrt(12)


def get_dipol_params_second_part(a1, da1, r, dr, r0, dr0):
    rt = r - r0, sqrt(dr ** 2 + dr0 ** 2)
    a1 = a1, da1
    d1 = rt[0] ** 3 * a1[1]
    d2 = 2 * rt[0] ** 2 * a1[0] * rt[1]
    return a1[0] * 2 * math.pi * rt[0] ** 3, 2 * math.pi * math.sqrt(d1 ** 2 + d2 ** 2)


def get_radial_magnetic_field(x, m=1, theta=0):
    return generate_field_radial_part(x, m, theta)


def first_fit(x, a2=1., a3=0.10, a1=Bearth[0], a4=3.):
    n = x - a3
    n = n + 0.001 if n == 0 else n
    derivatiive = n ** a4
    return (a1 + a2 / derivatiive) * electricity.MEUE_ZERO


def f1(x):
    return first_fit(x, 1 / 3000, a4=3.02)


def f2(x):
    return first_fit(x, 1 / 3000, a3=0.15)


def f3(x):
    return first_fit(x, 1 / 3000, a3=0.0510)


def f4(x):
    return first_fit(x, 31e4, a3=0.16)


def fit_fincs():
    return [f4]


def get_epsilon(x, A=2 * pi * R, B0=Bearth, omega=OUR_OMEGA):
    return A * B0 * omega * math.sin(omega * x)


def radial_magnetic_field_at_constant_r(x, B0=ELECTRIC_FIELD_AT_R, omega=OUR_OMEGA):
    return B0 * math.cos(omega * x)


if __name__ == '__main__':
    datax = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45]
    datax = [convertions.Lengths.cm_to_m(x) for x in datax]
    datay = [-0.17, -0.12, -0.087, -0.062, -0.043, -0.029, -0.017, -0.0091, -0.003, 0.003, 0.0072, 0.011, 0.014, 0.016,
             0.018, 0.02, 0.022, 0.023, 0.024, 0.025, 0.026]
    datay = [y for y in datay]
    plotting.plot_functions_and_data(fit_fincs(), datax, datay, step=0.001)
