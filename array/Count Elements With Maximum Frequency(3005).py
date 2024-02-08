class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        hash_nums = collections.Counter(nums)
        sorted_values = sorted(hash_nums.values(), reverse=True)
        counter = 0

        if len(set(sorted_values)) == 1:
            return sum(sorted_values)

        for i in range(len(sorted_values) - 1):
            if sorted_values[i] == sorted_values[i + 1]:
                counter += sorted_values[i]
            elif sorted_values[i] != sorted_values[i + 1]:
                counter += sorted_values[i]
                break
            elif sorted_values[i] == sorted_values[i - 1] and sorted_values[i] != sorted_values[i + 1]:
                counter += sorted_values[i]
                break

        return counter
