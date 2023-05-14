import collections


class Solution:
    def repeatedNTimes(self, nums) -> int:
        hash_num = collections.Counter(nums)
        result = 0

        for i in hash_num:
            if hash_num[i] > 1:
                result += i
        return result


