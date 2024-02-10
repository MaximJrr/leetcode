class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        counter = 0

        if nums == sorted_nums:
            return 0

        while nums != sorted_nums:
            if nums[-1] > nums[0]:
                return -1
            nums.insert(0, nums[-1])
            nums.pop()
            counter += 1

        return counter
