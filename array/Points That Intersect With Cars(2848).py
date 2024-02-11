class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        all_nums = []
        two_nums_pointer = 0
        first_num_pointer = 0
        second_num_pointer = 1
        hash_nums = {}
        counter = 0

        while two_nums_pointer < len(nums):
            all_nums.append([i for i in range(nums[two_nums_pointer][first_num_pointer], nums[two_nums_pointer][second_num_pointer] + 1)])
            two_nums_pointer += 1

        for i in all_nums:
            for j in i:
                if j not in hash_nums:
                    hash_nums[j] = 1
                    counter += 1

        return counter
