def greatestLetter(s: str) -> str:
    alphabet = [chr(i) for i in range(65, 91)]
    chars = ""

    for char in alphabet:
        if char in sorted(s) and char.lower() in sorted(s):
            chars = char
    return chars


if __name__ == '__main__':
    print(greatestLetter(s = "arRAzFif"))


