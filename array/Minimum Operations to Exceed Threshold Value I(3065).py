class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        counter = 0

        for num in nums:
            if num < k:
                counter += 1

        return counter
