class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        set_1 = set(nums1)

        for i in nums2:
            if i in set_1:
                return i

        return -1