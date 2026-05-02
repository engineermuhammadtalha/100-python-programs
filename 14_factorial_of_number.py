# solution 1 using for loop

num = int (input("enter a number here: "))
fact = 1
if num < 0:
    print("factorial does not exist for negative numbers")
if num == 0:
        print("the factorial of 0 is 1")
if num > 0:
    for i in range(1,num + 1):
        fact = fact * i
    print("the factorial of", num, "is", fact)
