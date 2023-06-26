class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        string_nums = list(map(str, nums))
        count = 0

        for i in string_nums:
            if len(i) % 2 == 0:
                count += 1
        return count