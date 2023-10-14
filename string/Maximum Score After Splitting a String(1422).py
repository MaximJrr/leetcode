class Solution:
    def maxScore(self, s: str) -> int:
        max_score = 0
        num_zeros_left = 0
        num_ones_right = s.count('1')

        for i in range(len(s) - 1):
            if s[i] == '0':
                num_zeros_left += 1
            else:
                num_ones_right -= 1
            max_score = max(max_score, num_zeros_left + num_ones_right)

        return max_score