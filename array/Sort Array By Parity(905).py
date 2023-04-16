class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        result = []

        for num in nums:
            if num % 2 == 0:
                result.append(num)

        for i in nums:
            if i % 2 == 1:
                result.append(i)

        return result