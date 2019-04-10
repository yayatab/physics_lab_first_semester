from general_tools.lab import n_sigma
from general_tools.general_math import *


def generate_phase_shift(A, B):
    return math.asin(B / A)


def phase_from_dt(omega, dt):
    return omega * dt


def vr_vo(R, omega, L, c):
    return R / sqrt(R ** 2 + (omega * L - 1 / (omega * c)))


def get_omega(L, DL, C, DC):
    return 1 / sqrt(L * C), 0.5 * sqrt(DC ** 2 / (L * C ** 3) + DL ** 2 / C * L ** 3)


def get_delta_omega(R, drt, L=23.91e-3, dl=1):
    d1 = drt / L
    d2 = (R * dl) / (L ** 2)
    return R / L, sqrt(d1 ** 2 + d2 ** 2)


def print_asins(A, B):
    for r in calc_asin_on_lists(A, B):
        print(r)


def generate_w0_anddelta_w_from_fit(a1, da1, a2, da2):
    w0 = 1 / sqrt(a1 * a2)
    dw0 = 0.5 * sqrt(da1 ** 2 / (a1 * a2 ** 3) + da2 ** 2 / (a2 * a1 ** 3))

    deltaw = 1 / a1
    deltadw = da1 / a1
    return (w0, dw0), (deltaw, deltadw)


def calc_n_sigma_for_w_and_dw(a1, a2):
    w, domega = generate_w0_anddelta_w_from_fit(*a1, *a2)
    omega_nsigma = n_sigma(*w_theo, *w)
    delta_omega_nsigma = n_sigma(*domega, *w0_theo)
    print("omega is", w)
    print("delta omega is", domega)
    print("nsigma_omega", omega_nsigma)
    print("nsigma_delta_omega", delta_omega_nsigma)
    return w, domega


if __name__ == '__main__':
    L = 0.8261
    C = 1.5e-9
    Rr = 6000

    dl = 46.305e-3
    dc = 0.048e-9
    a1 = (0.0002135697, 3.270912e-06)
    a2 = (7.665073e-06, 9.395436e-08)

    w_theo = get_omega(L=L, DL=dl, C=C, DC=dc)
    w0_theo = get_delta_omega(Rr, drt=150, L=L, dl=dl)
    print("w_theo", w_theo)
    print("w0_theo", w0_theo)
    w1, domega1 = calc_n_sigma_for_w_and_dw(a1, a2)

    a1 = (0.0002112431, 1.45986e-06)
    a2 = (7.733287e-06, 4.128126e-08)
    w2, domega2 = calc_n_sigma_for_w_and_dw(a1, a2)

    print("omegas nsigma", n_sigma(*w2, *w1))
    print("delta_omegas nsigma", n_sigma(*domega2, *domega1))
