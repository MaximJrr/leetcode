class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        seen_sums = {}

        for i in range(len(nums) - 1):
            current_sum = nums[i] + nums[i + 1]
            if current_sum in seen_sums and seen_sums[current_sum] != i:
                return True
            seen_sums[current_sum] = i

        return False