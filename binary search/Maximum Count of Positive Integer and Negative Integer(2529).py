class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        counter_1, counter_2 = 0, 0

    for num in nums:
        if num == 0:
            continue
        elif num > 0:
            counter_1 += 1
        else:
            counter_2 += 1
    return max(counter_1, counter_2)