class Solution:
    def findGCD(self, nums: List[int]) -> int:
        smallest_number = sorted(nums)[0]
        largest_number = sorted(nums)[-1]

        for num in range(smallest_number, 0, -1):
            if smallest_number % num == 0 and largest_number % num == 0:
                return num