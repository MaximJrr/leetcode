class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        string_nums = ''.join(list(map(str, nums)))
        result = []

        for num in string_nums:
            result.append(int(num))

        return result