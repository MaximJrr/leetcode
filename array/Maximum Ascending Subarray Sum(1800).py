class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        counter = nums[0]
        max_counter = nums[0]

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                counter += nums[i]
            else:
                counter = nums[i]
            max_counter = max(max_counter, counter)

        return max_counter

