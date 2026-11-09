"""Challenge 2: Read a joke file and imitate an Alexa joke request."""

import random
from pathlib import Path

JOKES_FILE = Path(__file__).with_name("randomJokes.txt")


def load_jokes():
    jokes = []
    with JOKES_FILE.open("r", encoding="utf-8-sig") as file:
        for line in file:
            if "?" not in line:
                continue
            setup, punchline = line.strip().split("?", 1)
            if setup.strip() and punchline.strip():
                jokes.append((setup.strip() + "?", punchline.strip()))
    return jokes


def main():
    try:
        jokes = load_jokes()
    except (OSError, UnicodeError) as error:
        print(f"Could not read {JOKES_FILE.name}: {error}")
        return

    if not jokes:
        print("No valid jokes were found in the file.")
        return

    print('Say "Alexa, tell me a joke" to hear a joke; type "quit" to exit.')
    while True:
        command = input("Your command: ").strip().lower()
        if command in ("quit", "exit"):
            print("Goodbye!")
            break
        if command in ("alexa, tell me a joke", "alexa tell me a joke"):
            setup, punchline = random.choice(jokes)
            print(setup)
            input("Press Enter for the punchline...")
            print(punchline)
        else:
            print('Please say "Alexa, tell me a joke", or "quit".')


if __name__ == "__main__":
    main()
