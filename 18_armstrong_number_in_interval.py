# armstrong number in [a,b]
def is_armstrong_number(num):
    # Convert number to string to easily iterate over digits
    digits = str(num)
    num_digits = len(digits)
    # Calculate the sum of each digit raised to the power of num_digits
    sum_of_powers = sum(int(digit) ** num_digits for digit in digits)

    # An Armstrong number is one where the sum of the powers equals the original number
    return sum_of_powers == num