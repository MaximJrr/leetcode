class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        total_sum = sum(nums)
        left_sum = 0

        for i in range(len(nums)):
            total_sum -= nums[i]

            if left_sum == total_sum:
                return i

            left_sum += nums[i]

        return -1
#