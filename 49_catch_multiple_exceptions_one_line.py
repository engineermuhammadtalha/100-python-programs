# 51) Multiple exceptions
try:
    x = 1/0
except (ZeroDivisionError, ValueError) as e:
    print("Error:", type(e).__name__)
# Output: Error: ZeroDivisionError