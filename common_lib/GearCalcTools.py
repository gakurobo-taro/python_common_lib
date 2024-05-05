"""
This module contains functions for calculating gear ratios, converting between centimeters and radians, and converting between degrees and radians.

Functions:

calc_gear(const: float, rad:float) -> float:
    This function calculates the gear ratio given the module and pitch of the gears.
    Args:
        const (float): Constant of the gear ratio.
        rad (float): Pitch of the gears in radians.
    Returns:
        float: Gear ratio.

calc_cm_to_rad(const: float, mm: float) -> float:
    This function converts centimeters to radians given a constant and a length in millimeters.
    Args:
        const (float): Constant of the conversion.
        mm (float): Length in millimeters.
    Returns:
        float: Length in radians.

calc_deg_to_rad(degrees: float) -> float:
    This function converts degrees to radians.
    Args:
        degrees (float): Angle in degrees.
    Returns:
        float: Angle in radians.
"""

import numpy as np

def calc_gear(const: float, rad:float) -> float:
    """
    This function calculates the gear ratio given the module and pitch of the gears.

    Args:
        const (float): Constant of the gear ratio.
        rad (float): Pitch of the gears in radians.

    Returns:
        float: Gear ratio.
    """
    return const * rad / (2 * np.pi)

def calc_cm_to_rad(const: float, mm: float) -> float:
    """
    This function converts centimeters to radians given a constant and a length in millimeters.

    Args:
        const (float): Constant of the conversion.
        mm (float): Length in millimeters.

    Returns:
        float: Length in radians.
    """
    return (2 * np.pi) * mm / const

def calc_deg_to_rad(degrees: float) -> float:
    """
    This function converts degrees to radians.

    Args:
        degrees (float): Angle in degrees.

    Returns:
        float: Angle in radians.
    """
    return degrees * np.pi / 180.0

import numpy as np

def calc_rad_to_cm(const: float, rad: float) -> float:
    """
    This function converts radians to centimeters given a constant and an angle in radians.

    Args:
        const (float): Constant of the conversion.
        rad (float): Angle in radians.

    Returns:
        float: Length in millimeters.
    """
    return const * rad / (2 * np.pi)