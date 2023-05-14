import collections


class Solution:
    def majorityElement(self, nums) -> int:
        hash_num = collections.Counter(nums)
        max_value = max(hash_num.values())

        for i in hash_num:
            if hash_num[i] == max_value:
                return i
