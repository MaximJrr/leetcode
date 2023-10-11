class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        result = 0
        left_p, right_p = 0, len(nums) - 1

        if len(nums) % 2 != 0:
            mid = left_p + right_p // 2
            result += nums[mid]

        while left_p < right_p:
            result += (int(str(nums[left_p]) + str(nums[right_p])))
            left_p += 1
            right_p -= 1
        return result