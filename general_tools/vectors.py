from math import sqrt, sin, cos, pi


def calc_length(vec):
    return sqrt(vec[0] ** 2 + vec[1] ** 2 + vec[2] ** 2)


def calc_x_y_rad(l, theta):
    return l * cos(theta), l * sin(theta)


def calc_x_y_deg(l, theta):
    theta = theta * pi / 180;
    return l * cos(theta), l * sin(theta)



