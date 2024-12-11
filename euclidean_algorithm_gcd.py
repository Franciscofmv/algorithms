
def gcd(a: int, b: int) -> int:
    """
    Euclidean algorithm to know the greatest common divisor.
    """

    if a == 0: 
        return b
    elif b == 0:
        return a
    else:
    
        # Do a = b*quotient + residue until (residue or b) == 0
        # GCD(A, B) == GCD(B,R)
        r = a % b
        return gcd(b, r)









def main():
    print(gcd(17, 3))

    
if __name__ == "__main__":
    main()