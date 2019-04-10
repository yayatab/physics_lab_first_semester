import math

import constants

MEUE_ZERO = 4 * constants.pi * 10 ** -7


def capacity_of_ball_si(radius=constants.EARTH_RADIUS):
    return 4 * constants.pi * constants.EPSILON_0 * radius


def generate_field_radial_part(radius, m, theta, u_0=MEUE_ZERO):
    """

    :param radius: the length from the magnet's center
    :param m: the dipol size
    :param theta: the angle in radians of the between teh dipol and the observation point
    :return:
    :rtype:
    """
    return (u_0 * m * math.cos(theta)) / (2 * constants.pi * radius ** 3)
