import math

def grams_to_ounces(grams):
    return grams * 28.3495231

def fahrenheit_to_celsius(f):
    return (5 / 9) * (f - 32)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def filter_prime(numbers):
    return [num for num in numbers if is_prime(num)]

def sphere_volume(radius):
    return (4 / 3) * math.pi * (radius ** 3)

