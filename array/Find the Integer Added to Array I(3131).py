class Solution:
    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()
        result = []

        for i, j in (zip(nums1, nums2)):
            result.append(j - i)

        return result[0]
