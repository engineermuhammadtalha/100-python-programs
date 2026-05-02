#quadratic equaton ax**2 + bx + c = 0
#a, b, c are real numbers and a != 0
import cmath

a = int(input("Enter number (a!=0): "))
b = int(input("Enter number: "))
c = int(input("Enter number: "))

#formula for discriminant
d= (b**2)  - (4*a*c)

#finding two solutions
root = (-b + cmath.sqrt(d)) / (2*a)
root2 = (-b - cmath.sqrt(d)) / (2*a)

print("the roots are " , root, "and", root2)
