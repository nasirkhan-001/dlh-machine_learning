#!/usr/bin/env python3
"""Module calculates the integral of polynomial"""


def poly_integral(poly, C=0):
    """integral coefficient = value divided by new power (i + 1)."""

    if not isinstance(poly, list) or len(poly) == 0:
        return None
    if not isinstance(C, int):
        return None

    # integration of constant fixed at zero rather 5x, 2x ..x etc
    new_poly = [C]
    for i in range(len(poly)):
        value = (poly[i] / (i + 1))
    # integral coeff if whole number and it must be without decimal
        if value == int(value):
            value = int(value)
        new_poly.append(value)
    return new_poly
