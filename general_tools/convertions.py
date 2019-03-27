class Lengths(object):
    @staticmethod
    def angstrom_to_cm(angs=1):
        return angs * 10e-8

    @staticmethod
    def cm_to_angstrom(cm=1):
        return cm * 10e8

    @staticmethod
    def m_to_cm(m=1):
        return m * 100

    @staticmethod
    def cm_to_m(cm=1):
        return cm / 100

    @staticmethod
    def km_to_m(km=1):
        return km * 1000


class Volumes(object):

    @staticmethod
    def m_to_cm(m3=1):
        return m3 * 10e6

    @staticmethod
    def cm_to_m(cm3=1):
        return cm3 * 10e-6

    @staticmethod
    def cm_to_angstrom(cm3=1):
        return cm3 * 10e24

    @staticmethod
    def angstrom_cm_to(ang=1):
        return ang * 10e-24

    @staticmethod
    def liter_to_m(l=1):
        return l * 0.001


class Areas(object):
    @staticmethod
    def cm_to_m(cm=1):
        return cm * 0.0001


class Pressures(object):
    @staticmethod
    def atm_to_pa(atm=1):
        return atm * 101325

    @staticmethod
    def pa_to_atm(pa=1):
        return pa * 9.86923267e-6

    @staticmethod
    def pa_to_mmHg(pa=1):
        return pa * 0.007501

    @staticmethod
    def mmHg_to_pa(mmHg=1):
        return mmHg * 133.322365
