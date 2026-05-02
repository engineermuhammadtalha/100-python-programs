#  Countdown timer (seconds)
import time
def countdown(n):
    while n:
        print(n, end="\r")
        time.sleep(1)
        n -= 1
    print("Done!")

# countdown(5)  # uncomment to run
