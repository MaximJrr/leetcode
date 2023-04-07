class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1, nums2 = sorted(nums1), sorted(nums2)
        pointer_1, pointer_2 = 0, 0
        result = []

        while pointer_1 < len(nums1) and pointer_2 < len(nums2):
            if nums1[pointer_1] < nums2[pointer_2]:
                pointer_1 += 1
            elif nums1[pointer_1] > nums2[pointer_2]:
                pointer_2 += 1
            else:
                result.append(nums1[pointer_1])
                pointer_1 += 1
                pointer_2 += 1
        return result