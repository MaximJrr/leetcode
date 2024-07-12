class Solution:
    def scoreOfString(self, s: str) -> int:
        result = 0

        for char in range(1, len(s)):
            result += (abs(ord(s[char - 1]) - ord(s[char])))

        return result
