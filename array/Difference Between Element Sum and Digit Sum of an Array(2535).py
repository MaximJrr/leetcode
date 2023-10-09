class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        sum_nums = sum(nums)
        string_nums = ''.join(list(map(str, nums)))
        counter = 0

        for num in string_nums:
            counter += int(num)

        return sum_nums - counter