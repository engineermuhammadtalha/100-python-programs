# Caesar Cipher - Encryption & Decryption

def caesar_cipher(text, shift, mode):
    result = ""
    if mode == "decrypt":
        shift = -shift
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

print("=== Caesar Cipher ===")
print("1. Encrypt")
print("2. Decrypt")
choice = input("Choose (1/2): ")

if choice in ("1", "2"):
    mode = "encrypt" if choice == "1" else "decrypt"
    text = input("Enter text: ")
    shift = int(input("Enter shift value (1-25): "))
    output = caesar_cipher(text, shift, mode)
    print(f"\n{mode.capitalize()}ed text: {output}")
else:
    print("Invalid choice.")
