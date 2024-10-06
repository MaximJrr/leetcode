class Solution:
    def minElement(self, nums: List[int]) -> int:
        result = []

        for num in nums:
            digit_sum = sum(int(digit) for digit in str(num))
            result.append(digit_sum)

        return min(result)
