"""
Basic number-theoretic functions used in cryptography and number theory.

This module contains simple and well-documented implementations
of the Extended Euclidean algorithm to compute the GCD of two integers
and the Bézout coefficients. 
"""

def extended_gcd(a: int, b: int) ->
    u, g, v, y = 1, a, 0, b
    while y !=0:
      u, g, v, y = v, y, u-(g//y)*v, a%b
    return (g,u,v)

if __name__ == "__main__":
    print(gcd(48, 18))   # expected: (6,-1,3)
    print(gcd(17, 5))    # expected: (1,-2,7)
    print(gcd(0, 7))     # expected: (7,0,1)



    
