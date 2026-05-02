#  Remove punctuation
import string
s = "Hello, world!"
print(''.join(ch for ch in s if ch not in string.punctuation))  # Output: Hello world
