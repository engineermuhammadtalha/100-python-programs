# armstrong checker (e.g.,153)
def is_armstrong(n):
	s = str(n)
	power = len(s)
	return n == sum(int(digit) ** power for digit in s)

print(is_armstrong(153))  # True