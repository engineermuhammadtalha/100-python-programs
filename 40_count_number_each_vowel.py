#  Vowel counts
s = "This is an example"
vowels = 'aeiou'
counts = {v: s.lower().count(v) for v in vowels}
print(counts)  # Output: counts per vowel
