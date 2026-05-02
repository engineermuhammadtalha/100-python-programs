# Number to Words Converter

ones = ["", "one", "two", "three", "four", "five", "six",
        "seven", "eight", "nine", "ten", "eleven", "twelve",
        "thirteen", "fourteen", "fifteen", "sixteen", "seventeen",
        "eighteen", "nineteen"]

tens = ["", "", "twenty", "thirty", "forty", "fifty",
        "sixty", "seventy", "eighty", "ninety"]

def number_to_words(n):
    if n == 0:
        return "zero"
    if n < 0:
        return "negative " + number_to_words(-n)
    if n < 20:
        return ones[n]
    if n < 100:
        return tens[n // 10] + ("" if n % 10 == 0 else "-" + ones[n % 10])
    if n < 1000:
        return ones[n // 100] + " hundred" + ("" if n % 100 == 0 else " " + number_to_words(n % 100))
    if n < 1_000_000:
        return number_to_words(n // 1000) + " thousand" + ("" if n % 1000 == 0 else " " + number_to_words(n % 1000))
    return "Number too large"

num = int(input("Enter a number (up to 999,999): "))
print(f"{num} = {number_to_words(num)}")
