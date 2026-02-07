"""
Basic number-theoretic functions used in cryptography and number theory.

This module contains simple and well-documented implementations
of the Extended Euclidean algorithm to compute the GCD of two integers
and the Bézout coefficients. 
"""

def extended_gcd(a: int, b: int) -> tuple[int, int, int]:
    """
    Compute the greatest common divisor g of a and b together with the Bézout coefficient (u,v) for the relation ua+vb=g.

    Parameters
    ----------
    a : int
        An Integer.
    b : int
        An Integer.

    Returns
    -------
    (g,u,v)
     g: int
        The greatest common divisor of a and b (always non-negative).
     u: int
        The Bézout coefficient for a.
     v: int 
        The Bézout coefficient for b.
    """

    u, g, v, y = 1, a, 0, b
    while y !=0:
      u, g, v, y = v, y, u-(g//y)*v, g%y
    
    # Ensure GCD is non-negative.
    if g<0:
        g=-g
        u=-u
        v=-v
    
    return (g,u,v)

if __name__ == "__main__":
    print(extended_gcd(48, 18))   # expected: (6,-1,3)
    print(extended_gcd(17, 5))    # expected: (1,-2,5)
    print(extended_gcd(0, 7))     # expected: (7,0,1)



    
