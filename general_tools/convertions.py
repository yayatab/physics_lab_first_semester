class Lengths(object):
    @staticmethod
    def angstrom_to_cm(angs):
        return angs * 10e-8

    @staticmethod
    def cm_to_angstrom(cm):
        return cm * 10e8

    @staticmethod
    def m_to_cm(m):
        return m * 100

    @staticmethod
    def cm_to_m(cm):
        return cm / 100


class Volumes(object):

    @staticmethod
    def m_to_cm(m3):
        return m3 * 10e6

    @staticmethod
    def cm_to_m(cm3):
        return cm3 * 10e-6

    @staticmethod
    def cm_to_angstrom(cm3):
        return cm3 * 10e24

    @staticmethod
    def angstrom_cm_to(ang):
        return ang * 10e-24

    @staticmethod
    def liter_to_m(l):
        return l * 0.001


class Areas(object):
    @staticmethod
    def cm_to_m(cm):
        return cm * 0.0001


class Pressures(object):
    @staticmethod
    def atm_to_pa(atm):
        return atm * 101325

    @staticmethod
    def pa_to_mmHg(pa):
        return pa * 0.007501

    @staticmethod
    def mmHg_to_pa(mmHg):
        return mmHg * 133.322365
