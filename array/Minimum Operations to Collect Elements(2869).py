class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        hash_nums = {}
        counter = 0

        for i in range(1, k + 1):
            hash_nums[i] = None

        while None in hash_nums.values():
            last_num = nums.pop()
            if last_num in hash_nums:
                hash_nums[last_num] = last_num
            counter += 1

        return counter
