class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        result_1 = []
        result_2 = []

        for i in nums1:
            if i not in nums2:
                result_1.append(i)

        for i in nums2:
            if i not in nums1:
                result_2.append(i)

        return [list(set(result_1)), list(set(result_2))]