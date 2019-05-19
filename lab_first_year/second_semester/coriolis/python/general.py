from general_tools.lab import FitObject, calc_sigma_div
from math import sqrt


def omega(t: FitObject):
    dt = t.err / t.val ^ 2
    return 1 / T.val, dt


T = FitObject(2.735333, 0.365586)
OMEGA = FitObject(*omega(T))
RADIUS = FitObject(0.2, 0.00122)  # meter


class Lin(object):
    @staticmethod
    def extract_v0(a: FitObject, omega=OMEGA, r=RADIUS):
        d1 = omega * r * a.err
        d2 = omega * a * r.err
        d3 = r * a * omega.err
        dv = calc_sigma_div(d1, d2, d3)
        return FitObject(a * omega * r, dv)

    @staticmethod
    def extract_r(b):
        return FitObject(-b, b.err)


class Parabol(object):
    @staticmethod
    def extract_r(c: FitObject):
        return FitObject(sqrt(c.val), c.err / (2 * sqrt(c.val)))

    @staticmethod
    def extract_vo_from_t(b: FitObject, omega=OMEGA, r=RADIUS):
        val = -1 * b / (2 * omega * r)
        d1 = b.err / (2 * omega * r)
        d2 = b * omega.err / (2 * r * omega ** 2)
        d3 = b * r.err / (2 * omega * r ** 2)
        return FitObject(val, calc_sigma_div(d1, d2, d3))

    @staticmethod
    def extract_vo_from_tsqr(a: FitObject, omega=OMEGA, r=RADIUS):
        val = sqrt(a - (omega * r ** 2))
        d1 = a.err / (2 * val)
        d2 = (omega * r ** 2 * omega.err) / val
        d3 = (r * omega ** 2 * r.err) / val
        return FitObject(val, calc_sigma_div(d1, d2, d3))

