class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        intersection_1 = set(nums1).intersection(set(nums2))
        intersection_2 = set(nums2).intersection(set(nums3))
        intersection_3 = set(nums1).intersection(set(nums3))
        return list(set(list(intersection_1) + list(intersection_2) + list(intersection_3)))
