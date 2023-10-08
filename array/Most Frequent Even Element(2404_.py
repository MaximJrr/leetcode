class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        hash_nums = {}

        for num in nums:
            if num % 2 == 0:
                hash_nums[num] = hash_nums.get(num, 0) + 1

        most_frequent_even = -1
        max_frequency = 0

        for num, frequency in hash_nums.items():
            if frequency > max_frequency or (frequency == max_frequency and num < most_frequent_even):
                most_frequent_even = num
                max_frequency = frequency

        return most_frequent_even
