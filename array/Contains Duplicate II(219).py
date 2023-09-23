class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        nums_indices = {}

        for i, num in enumerate(nums):
            if num in nums_indices and i - nums_indices[num] <= k:
                return True
            nums_indices[num] = i

        return False