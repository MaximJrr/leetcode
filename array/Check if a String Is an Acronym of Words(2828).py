class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        words_pointer = 0
        s_pointer = 0

        if len(words) != len(s):
            return False

        while words_pointer < len(words):
            if words[words_pointer][0] == s[s_pointer]:
                words_pointer += 1
                s_pointer += 1
                continue
            return False

        return True
