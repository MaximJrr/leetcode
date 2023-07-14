class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        counter = 0
        hash_nums = collections.Counter(nums)

        for i in hash_nums:
            if hash_nums[i] == 1:
                counter += i
        return counter
