class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        result = 0
        word = set(word)
        hashed_lower = set()
        hashed_upper = set()

        for i in word:
            if i.islower():
                hashed_lower.add(i)
            elif i.isupper():
                hashed_upper.add(i)

        for char in hashed_lower:
            if char.capitalize() in hashed_upper:
                result += 1

        return result
