#Write a Python program to calculate surface volume and area of a cylinder


import math

def cylinder(r,h):
    return math.pi * r ** 2 * h

def cylinder_surface(r,h):
    return 2 * math.pi * r * (r + h) 

r = float(input("Enter your radius:"))
h = float(input("Enter your hight"))

volume = cylinder(r, h)
surface_area = cylinder_surface(r, h)

print("Volume of cylinder area: ", volume)
print("Surface area of cylinder: ", surface_area)

