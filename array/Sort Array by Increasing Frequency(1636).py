class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq_dict = collections.Counter(nums)
        nums.sort(key=lambda x: (freq_dict[x], -x))

        return nums