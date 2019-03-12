from math import sqrt, sin, cos, pi


def calc_length(vec):
    return sqrt(sum(i**2 for i in vec))


def calc_x_y_rad(l, theta):
    return l * cos(theta), l * sin(theta)


def calc_x_y_deg(l, theta):
    theta = theta * pi / 180
    return l * cos(theta), l * sin(theta)



