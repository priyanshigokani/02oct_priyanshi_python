#Write a Python program to calculate the area of a trapezoid

def trapezoid(x,y,h):
    area = 0.5*(x + y)*h
    return area

x = float(input("Enter x:"))
y = float(input("Enter y:"))
h = float(input("Enter h:"))

area = trapezoid(x,y,h)

print("Area of trapezoid is: " ,area)