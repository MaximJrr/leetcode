class Solution:
    def largestInteger(self, num: int) -> int:
        even_digits = sorted([i for i in str(num) if int(i) % 2 == 0], reverse=True)
        odd_digits = sorted([i for i in str(num) if int(i) % 2 != 0], reverse=True)
        even_index = 0
        odd_index = 0
        result = []

        for i in str(num):
            if int(i) % 2 == 0:
                result.append(even_digits[even_index])
                even_index += 1
            else:
                result.append(odd_digits[odd_index])
                odd_index += 1

        return int(''.join(result))
