# Typing Speed Test
import time
import random

sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "Python is a powerful and easy to learn programming language.",
    "Practice makes perfect when it comes to typing speed.",
    "Every great programmer was once a beginner who never gave up.",
    "Hard work and consistency are the keys to success in coding."
]

def typing_speed_test():
    sentence = random.choice(sentences)
    print("\n=== Typing Speed Test ===")
    print("Type the following sentence:")
    print(f"\n  {sentence}\n")
    input("Press Enter when ready...")

    start_time = time.time()
    user_input = input("Start typing:\n")
    end_time = time.time()

    elapsed = end_time - start_time
    words = len(sentence.split())
    wpm = (words / elapsed) * 60

    correct_chars = sum(1 for a, b in zip(sentence, user_input) if a == b)
    accuracy = (correct_chars / len(sentence)) * 100

    print(f"\n--- Results ---")
    print(f"Time Taken : {elapsed:.2f} seconds")
    print(f"Speed      : {wpm:.1f} WPM")
    print(f"Accuracy   : {accuracy:.1f}%")

    if user_input.strip() == sentence.strip():
        print("✅ Perfect typing!")
    else:
        print("❌ Some mistakes were made.")

typing_speed_test()
