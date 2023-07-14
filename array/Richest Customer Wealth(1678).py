class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        acc_sum = []

        for i in accounts:
            acc_sum.append(sum(i))
        return max(acc_sum)
