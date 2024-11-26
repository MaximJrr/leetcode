class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        left_pointer = 0
        right_pointer = len(nums) - 1
        averages = []
        nums.sort()

        while len(averages) != len(nums) // 2:
            min_element = nums[left_pointer]
            max_element = nums[right_pointer]
            averages.append((min_element + max_element) / 2)
            left_pointer += 1
            right_pointer -= 1

        return min(averages)
