class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        count = 0

        for l in range(len(nums)):
            for r in range(l + 1, len(nums)):
                if nums[l] - nums[r] == k or nums[r] - nums[l] == k:
                    count += 1
        return count
