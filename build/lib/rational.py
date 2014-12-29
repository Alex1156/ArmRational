from math import copysign


def gcd(a, b):
    """Computes greatest common divisor of two values"""
    if b == 0:
        return a
    return gcd(b, a % b)


class Rational:
    """Representation of rational number
    >>> Rational(1,2)
    1/2
    >>> Rational(2,4)
    1/2
    >>> Rational(1,2) + Rational(3,4)
    5/4
    >>> Rational(-1,2)
    -1/2
    >>> Rational(5)
    5
    >>> float(Rational(3,4))
    0.75
    """

    def __init__(self, top=1, bottom=1):
        """Initializes Rational instance"""

        # do not allow 0 d
        if bottom == 0:
            raise ZeroDivisionError("Cannot have 0 d")

        # assign attribute values
        self.n = abs(top)
        self.d = abs(bottom)
        self.sign = copysign(1, top * bottom)

    def __add__(self, other):
        return Rational(self.sign * self.n * other.d + other.sign * other.n * self.d, self.d * other.d)

    def __sub__(self, other):
        return self + (-other)

    def __mul__(self, other):
        pass

    def __divmod__(self, other):
        pass

    def __str__(self):
        return "{}/{}".format(self.n, self.d)

    __repr__ = __str__

    def __float__(self):
        pass


if __name__ == '__main__':
    import doctest

    doctest.testmod()
    x = Rational(-1, 2) + Rational(1, 3)
    print(x)




