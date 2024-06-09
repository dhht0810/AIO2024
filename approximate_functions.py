import math

def approximate_sin(x, n = 5):
    result = 0
    for n in range(n):
        numerator = (-1) ** n * x ** (2 * n + 1)
        denominator = math.factorial(2 * n + 1)
        result += numerator / denominator
    return result

def approximate_cos(x, n = 5):
    result = 0
    for n in range(n):
        numerator = (-1) ** n * x ** (2 * n)
        denominator = math.factorial(2 * n)
        result += numerator / denominator
    return result

def approximate_cosh(x, n = 5):
    result = 0
    for n in range(n):
        numerator = x ** (2 * n)
        denominator = math.factorial(2 * n)
        result += numerator / denominator
    return result

def approximate_sinh(x, n = 5):
    result = 0
    for n in range(n):
        numerator = x ** (2 * n + 1)
        denominator = math.factorial(2 * n + 1)
        result += numerator / denominator
    return result

# Example usage
x = 3.14
n = 10
print(approximate_sin(x, n))
print(approximate_cos(x, n))
print(approximate_cosh(x, n))
print(approximate_sinh(x, n))