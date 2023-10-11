class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        result = []

        for num in range(len(nums)):
            left_sum = sum(nums[:num])
            right_sum = sum(nums[num + 1:])
            result.append(abs(left_sum - right_sum))

        return result