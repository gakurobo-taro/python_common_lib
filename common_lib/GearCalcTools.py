import numpy as np

def calc_gear(const: float, rad:float) -> float:
    return const * rad / (2 * np.pi)

def calc_cm_to_rad(const: float, mm: float) -> float:
    return (2 * np.pi) * mm / const

def calc_deg_to_rad(degrees: float) -> float:
    return degrees * np.pi / 180.0