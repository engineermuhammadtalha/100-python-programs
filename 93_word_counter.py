# Word Counter

text = input("Enter a sentence or paragraph:\n")

word_count = len(text.split())
char_count = len(text)
char_no_space = len(text.replace(" ", ""))
sentence_count = text.count('.') + text.count('!') + text.count('?')

print("\n--- Word Counter Results ---")
print(f"Words       : {word_count}")
print(f"Characters  : {char_count}")
print(f"Chars (no spaces): {char_no_space}")
print(f"Sentences   : {sentence_count}")
