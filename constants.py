from math import pi
from scipy import constants as con
from scipy.constants import find as fnd
from general_tools.convertions import Lengths

AVOGADRO_NUMBER = 6.022140857e23
G_THEO_CM = 981.3
G_THEO_CM_D = 10
G_THEO = G_THEO_CM / 100
G_THEO_D = G_THEO_CM_D / 100
EPSILON_0 = 8.854187817e-12
EARTH_RADIUS = 6_371_000


def find_constant(name=None) -> dict:
    """
    returns a dictionary of the constant name and it's value:
    for example:
    !!! ALL THE CONSTANTS ARE IN SI UNITS !!!
    :param name:
    :type name: str
    :return: dictionary of name and value
    :rtype: dict
    """
    res = fnd(name)
    if res is None:
        print("constant not found")
    else:
        ret = {}
        for key in res:
            ret.update({key: [con.value(key), con.unit(key)]})
        return ret


def get_units(something: str):
    return con.unit(something)
