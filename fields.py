class FiniteField:
    """
    A class for arithmetic in a finite field F_q.
    This is a prime field implementation for simplicity.
    """

    def __init__(self, prime: int):
        self.prime = prime

    def add(self, a: int, b: int) -> int:
        return (a + b) % self.prime

    def mul(self, a: int, b: int) -> int:
        return (a * b) % self.prime

    def pow(self, base: int, exponent: int) -> int:
        # Modular exponentiation
        return pow(base, exponent, self.prime)

    def inv(self, a: int) -> int:
        # Modular inverse using Fermat's Little Theorem
        return self.pow(a, self.prime - 2)