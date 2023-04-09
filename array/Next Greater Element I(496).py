class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        temp_stack, num_dict = [], {}

        for i in nums2:
            while temp_stack and temp_stack[-1] < i:
                num_dict[temp_stack.pop()] = i
            else:
                temp_stack.append(i)

        for num in range(len(nums1)):
            if nums1[num] in num_dict:
                nums1[num] = num_dict[nums1[num]]
            else:
                nums1[num] = -1
        return nums1
