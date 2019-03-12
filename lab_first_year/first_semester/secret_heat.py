from general_tools.lab import *


def delta_l(v, i, dvdt, di, dv, ddmdt):
    d1 = (v * i / (dvdt) ** 2) * ddmdt
    d2 = (i * dv) / ddmdt
    d3 = (di * v) / ddmdt

    return sqrt(sum([x ** 2 for x in [d1, d2, d3]]))
