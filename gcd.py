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
    
    if __name__ == "__main__":
    print(gcd(48, 18))   # expected: 6
    print(gcd(17, 5))    # expected: 1
    print(gcd(0, 7))     # expected: 7
