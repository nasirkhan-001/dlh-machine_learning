#!/usr/bin/env python3
"""Module calculates the integral of polynomial"""


def poly_integral(poly, C=0):
    """integral coefficient = add 1 to power → divide by new power."""

    if not isinstance(poly, list) or len(poly) == 0:
        return None
    for element in poly:
        if not isinstance(element, (int, float)):
            return None

    # base case derivative, like for constant its zero
    if len(poly) == 1:
        return [0]

    # derivative of function above constant
    new_poly = []
    for i in range(1, len(poly)):
        new_poly.append(i * poly[i])
    return new_poly
