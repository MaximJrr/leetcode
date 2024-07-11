class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        result = 0
        hashed_t = {}

        for index, char in enumerate(t):
            hashed_t[char] = index

        for i in range(len(s)):
            first = i
            second = hashed_t[s[i]]
            if second > first:
                diff = second - first
                result += diff
            if first > second:
                diff = first - second
                result += diff

        return result
