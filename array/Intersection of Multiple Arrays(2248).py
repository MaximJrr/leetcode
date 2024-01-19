class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        hash_nums = {}
        result = []

        for i in nums:
            for j in i:
                if j not in hash_nums:
                    hash_nums[j] = 1
                elif j in hash_nums:
                    hash_nums[j] += 1

        for num in hash_nums:
            if hash_nums[num] == len(nums):
                result.append(num)

        return sorted(result)
