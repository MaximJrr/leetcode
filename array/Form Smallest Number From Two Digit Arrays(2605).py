class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        min_nums = sorted(str(min(nums1)) + str(min(nums2)))

        for num in sorted(nums1):
            if num in nums2:
                return num
            else:
                continue
        return int(''.join(min_nums))