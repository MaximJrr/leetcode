class Solution:
    def averageValue(self, nums: List[int]) -> int:
        result = 0
        counter = 0

        for num in nums:
            if num % 2 == 0 and num % 3 == 0:
                result += num
                counter += 1

        if counter == 0:
            return 0

        return result // counter
