class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        positive = []
        negative = []

        for num in nums:
            if num > 0:
                positive.append(num)
            else:
                negative.append(abs(num))

        sorted_positive = sorted(positive)[::-1]
        sorted_negative = sorted(negative)[::-1]
        hash_positive = collections.Counter(sorted_positive)
        hash_negative = collections.Counter(sorted_negative)

        for i in hash_positive:
            if i in hash_negative:
                return i
        return -1
