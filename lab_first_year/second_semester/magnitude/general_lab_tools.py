from constants import pi
from general_tools.electricity import generate_field_radial_part
from general_tools.lab import n_sigma
from general_tools.general_math import *
from general_tools import plotting, convertions, electricity

R = 13  # in cm
ELECTRIC_FIELD_AT_R = 12  # todo calc
OUR_OMEGA = 30

Bearth = (0.039, 3.65E-04)


def get_dipol_params(a1, da1, r, dr, r0, dr0):
    # todo chekc for correctnes
    tpi = 2 * pi
    m_r = (tpi * a1, tpi * da1)
    delta_r = (r - r0)
    m_theta = m_r[0] * delta_r ** 3
    d1 = da1 * delta_r ** 3
    d2 = 3 * a1 * delta_r ** 2 * dr
    delta_m_theta = tpi * sqrt(d1 ** 2 + 2 * d2 ** 2)
    return m_r, (m_theta, delta_m_theta)


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
    return first_fit(x, 31e4 , a3=0.16)


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
