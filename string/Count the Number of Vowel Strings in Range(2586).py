class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        counter = 0
        chars = ['a', 'e', 'i', 'o', 'u']

        for i in range(left, right + 1):
            if words[i][0] in chars and words[i][-1] in chars:
                counter += 1
        return counter