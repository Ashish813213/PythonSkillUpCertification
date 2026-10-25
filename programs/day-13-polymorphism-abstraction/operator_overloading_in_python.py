# Operator overloading: add two complex numbers with + and print as "a + bi".
class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)

    def __str__(self):
        return "{} + {}i".format(self.real, self.imaginary)
