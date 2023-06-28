class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        result = ''
        last_pointer = len(num) - 1
        if num[-1] != '0':
            return num
        if num == '0':
            return ''

        while last_pointer >= 0:
            if num[last_pointer] == '0':
                last_pointer -= 1
            else:
                result = num[:last_pointer + 1]
                break

        return result