import math
class Calculator:
    def add(self, a, b):
        return a + b
    def subtract(self, a, b):
        return a - b
    def multiply(self, a, b):
        return a * b
    def divide(self, a, b):
        if b == 0:
            raise valueError("Cannot divide by zero")
        return a / b

    def square_root(self, x):
        return math.sqrt(x)
