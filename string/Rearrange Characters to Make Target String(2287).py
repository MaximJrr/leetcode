class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        hash_s = collections.Counter(s)
        hash_target = collections.Counter(target)
        min_ratio = float('inf')

        for letter in target:
            if letter not in hash_s:
                return 0
            ratio = hash_s[letter] // hash_target[letter]
            min_ratio = min(min_ratio, ratio)

        return min_ratio