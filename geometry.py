# This program contains functions that evaluate formulas used in geometry.
#
# Your Name
# August 22, 2014

import math

def triangle_area(b, h):
    a = (1/2) * b * h
    return a

def circle_area(r):
    a = math.pi * r**2
    return a

def parallelogram_area(b, h):
    a = b * h
    return a

def trapezoid_area (a, b, h):
    A = (a + b / 2) * h
    return A

def rectangle_prism_area (l, w, h):
    v = l * w * h
    return v

def cone_volume (r, h):
    a = (math.pi * r ** 2) * (h / 3)
    return a

def sphere_volume (r):
    v = 4 / 3 * math.pi * r ** 3
    return v

def sa_rec_prism (l, w, h):
    a = 2 * (w * l + h * l + h * w)
    return a

def sa_sphere (r):
    a = 4 * math.pi * r ** 2
    return a

def hype_right_triangle (b, c):
    a = (b ** 2 + c ** 2) ** .5
    return a

def herons_formula(a, b, c):
    s = (a + b + c) / 2
    z = (s * (s - a) * (s - b) * (s - c)) ** .5
    return z

# function calls
    print(triangle_area(4,9))
print(circle_area(5))
print(circle_area(12))
print(parallelogram_area(5,6))
print(trapezoid_area(1, 2, 3))
print(rectangle_prism_area(5, 5, 5))
print(cone_volume(2, 5))
print(sphere_volume(5))
print(sa_rec_prism(5, 5, 5))
print(sa_sphere(4))
print(hype_right_triangle(5, 7))
print(herons_formula(3, 8, 12))

                



