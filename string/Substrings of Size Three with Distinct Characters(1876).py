class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        count = 0

        for char in range(len(s) - 2):
            if s[char] != s[char + 1] and s[char] != s[char + 2] and s[char + 1] != s[char + 2]:
                count += 1

        return count