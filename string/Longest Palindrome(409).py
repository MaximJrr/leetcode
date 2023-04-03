import collections


class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = 0
        odd = 0
        hash_s = collections.Counter(s)

        for i in hash_s:
            if hash_s[i] % 2 == 0:
                count += hash_s[i]
            else:
                count += hash_s[i] - 1
                odd = 1
        return count + odd