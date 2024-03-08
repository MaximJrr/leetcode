class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        pointer = 0
        result = []

        while pointer < len(number):
            if int(number[pointer]) == int(digit):
                result.append(int(number[:pointer] + (number[pointer + 1:])))
            pointer += 1

        return str(max(result))
