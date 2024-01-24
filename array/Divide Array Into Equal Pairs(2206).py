class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        hash_nums = collections.Counter(nums)

        for i in hash_nums.values():
            if i % 2 != 0:
                return False

        return True
