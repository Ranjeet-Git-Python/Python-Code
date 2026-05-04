#Question: Write a Python program to solve a quadratic equation of the form ax^2 + bx + c = 0, where a, b, and c are coefficients provided by the user. The program should calculate the discriminant and determine the nature of the roots (real and distinct, real and equal, or complex) and then print the roots accordingly.
import math

def main():
    a = float(input("Enter coefficient a: "))
    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))
    
    discriminant = b**2 - 4*a*c
    
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        print(f"Two real roots: {root1} and {root2}")
    elif discriminant == 0:
        root = -b / (2*a)
        print(f"One real root: {root}")
    else:
        real_part = -b / (2*a)
        imag_part = math.sqrt(-discriminant) / (2*a)
        print(f"Complex roots: {real_part} + {imag_part}i and {real_part} - {imag_part}i")

if __name__ == "__main__":
    main()