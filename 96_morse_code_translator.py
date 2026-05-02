# Morse Code Translator

MORSE_CODE = {
    'A': '.-',   'B': '-...', 'C': '-.-.', 'D': '-..',
    'E': '.',    'F': '..-.', 'G': '--.',  'H': '....',
    'I': '..',   'J': '.---', 'K': '-.-',  'L': '.-..',
    'M': '--',   'N': '-.',   'O': '---',  'P': '.--.',
    'Q': '--.-', 'R': '.-.',  'S': '...',  'T': '-',
    'U': '..-',  'V': '...-', 'W': '.--',  'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..',  '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', ' ': '/'
}

REVERSE_MORSE = {v: k for k, v in MORSE_CODE.items()}

def to_morse(text):
    return ' '.join(MORSE_CODE.get(c.upper(), '?') for c in text)

def from_morse(code):
    return ''.join(REVERSE_MORSE.get(c, '?') for c in code.split())

print("1. Text to Morse")
print("2. Morse to Text")
choice = input("Choose (1/2): ")

if choice == "1":
    text = input("Enter text: ")
    print("Morse Code:", to_morse(text))
elif choice == "2":
    code = input("Enter morse code (use space between letters, / for space): ")
    print("Text:", from_morse(code))
else:
    print("Invalid choice.")
