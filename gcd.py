"""
Basic number-theoretic functions used in cryptography.

This module contains simple and well-documented implementations
of the Euclidean algorithm and related routines.
"""


def gcd(a: int, b: int) -> int:
    """
    Compute the greatest common divisor of a and b.

    Parameters
    ----------
    a : int
        An integer.
    b : int
        An integer.

    Returns
    -------
    int
        The greatest common divisor of a and b.
    """
    while b != 0:
        a, b = b, a % b
    return abs(a)
