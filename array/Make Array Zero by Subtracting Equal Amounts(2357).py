class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        res = []

        for num in nums:
            if num in res or num == 0:
                continue
            res.append(num)

        return len(res)