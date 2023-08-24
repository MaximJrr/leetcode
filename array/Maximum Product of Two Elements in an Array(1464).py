class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        first_num = sorted_nums[-1]
        second_nums = sorted_nums[-2]

        return (first_num - 1) * (second_nums - 1)