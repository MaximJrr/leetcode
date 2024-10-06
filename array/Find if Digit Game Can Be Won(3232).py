class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        single_digit_counter = 0
        double_digit_counter = 0

        for num in nums:
            if num < 10:
                single_digit_counter += num
            elif num >= 10:
                double_digit_counter += num

        if single_digit_counter > double_digit_counter:
            return True
        elif single_digit_counter < double_digit_counter:
            return True

        return False
