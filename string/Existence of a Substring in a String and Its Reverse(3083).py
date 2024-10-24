class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        reversed_s = s[::-1]

        first_char_pointer = 0
        second_char_pointer = 1

        while second_char_pointer < len(s):
            if s[first_char_pointer] + s[second_char_pointer] in reversed_s:
                return True
            else:
                first_char_pointer += 1
                second_char_pointer += 1

        return False
