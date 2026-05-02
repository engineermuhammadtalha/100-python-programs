#solution1 (using exponentiation)
""" num = 64
num1 = int(input("Enter a number to find the square root: "))
square_root = num1 ** (1/2) or  0.5
print("The square root of", num1, "is", square_root)"""
 

 #solution2 (using math module)
import math
num1 = int(input("Enter a number to find the square root: "))
square_root = math.sqrt(num1)
print("The square root of", num1, "is", square_root)