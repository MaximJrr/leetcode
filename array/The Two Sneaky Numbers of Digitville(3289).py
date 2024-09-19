class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        hash_nums = {}
        result = []

        for num in nums:
            if num not in hash_nums:
                hash_nums[num] = 1
            elif num in hash_nums:
                hash_nums[num] += 1

        for i in hash_nums:
            if hash_nums[i] > 1:
                result.append(i)

        return result
