class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        result = []

        for num in nums:
            result.append(num)

        for i in nums:
            result.append(i)

        return result
