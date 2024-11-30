class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        result = 0
        pointer = 0

        while pointer < len(nums):
            result += nums[pointer]
            pointer += 2

        return result
