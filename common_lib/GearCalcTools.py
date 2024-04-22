import numpy as np

def calc_gear(const, rad):
    return const * rad / (2 * np.pi)

def calc_cm_to_rad(const, mm):
    return (2 * np.pi) * mm / const

def calc_deg_to_rad(degrees):
    return degrees * np.pi / 180.0