class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        all_nums = []
        repeat_num = []
        result = [[0], [1]]
        repeat_num_pointer = 0
        p = 1

        for i in grid:
            for j in i:
                all_nums.append(j)

        while repeat_num_pointer < len(all_nums):
            if all_nums[repeat_num_pointer] in repeat_num:
                result[0] = all_nums[repeat_num_pointer]
            else:
                repeat_num.append(all_nums[repeat_num_pointer])
            repeat_num_pointer += 1
            if p not in all_nums:
                result[1] = p
            p += 1

        return result
