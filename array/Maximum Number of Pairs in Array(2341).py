class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        hash_nums = collections.Counter(nums)
        pairs_count = 0
        leftover_count = 0

        for val in hash_nums.values():
            pairs_count += val // 2
            leftover_count += val % 2

        return [pairs_count, leftover_count]
