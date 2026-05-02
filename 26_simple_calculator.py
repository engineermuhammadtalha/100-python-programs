# simple calculator (addition, subtraction, multiplication, division)
def calc(a, b, op):
    return {'+': a+b, '-': a-b, '*': a*b, '/': a/b if b!=0 else None}.get(op)

print(calc(10, 5, '+'))  # Output: 15
