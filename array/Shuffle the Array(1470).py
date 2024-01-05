class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        left_nums = []
        right_nums = []
        result = []

        for num in range(n):
            left_nums.append(nums[num])

        for num in range(n, len(nums)):
            right_nums.append(nums[num])

        for i, j in zip(left_nums, right_nums):
            result.append(i)
            result.append(j)

        return result
