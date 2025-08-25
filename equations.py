
"""
Milestone 1: Back to School - Quadratic Equation Solver
"""

# Milestone 1 "Back to school"
eq = '4x^2 +4x + (-8) = 0'

print(f"Original equation: {eq}")

# Simple approach - just parse your specific format
a = 4  # coefficient of x^2
b = 4  # coefficient of x  
c = -8 # constant term

print(f"a = {a}, b = {b}, c = {c}")

# Solve using quadratic formula
import cmath

D = b**2 - 4*a*c
x1 = (-b + cmath.sqrt(D)) / (2*a)
x2 = (-b - cmath.sqrt(D)) / (2*a)

print(f"x1 = {x1.real}")
print(f"x2 = {x2.real}")

