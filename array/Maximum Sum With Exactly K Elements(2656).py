class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        nums.sort()
        result = []

        while k > 0:
            last_num = nums.pop()
            result.append(last_num)
            nums.append(result[-1] + 1)
            k -= 1

        return sum(result)