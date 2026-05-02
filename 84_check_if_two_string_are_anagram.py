# 84) Anagram check
def is_anagram(a, b):
    return sorted(a.replace(" ","").lower()) == sorted(b.replace(" ","").lower())

print(is_anagram("listen", "silent"))  # Output: True
