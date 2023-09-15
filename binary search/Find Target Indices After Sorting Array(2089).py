class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        sorted_nums = sorted(nums)
        result = []

        for num in range(len(sorted_nums)):
            if sorted_nums[num] == target:
                result.append(num)
        return result
        
