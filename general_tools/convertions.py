class Lengths(object):
    @staticmethod
    def angstrem_to_cm(angs):
        return angs * 10e-8

    @staticmethod
    def cm_to_angstrem(cm):
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