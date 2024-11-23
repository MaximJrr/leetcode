class Solution:
    def isBalanced(self, num: str) -> bool:
        sum_1 = 0
        sum_2 = 0

        for index, number in enumerate(num):
            if index % 2 == 0:
                sum_2 += int(number)
            else:
                sum_1 += int(number)

        if sum_1 == sum_2:
            return True
        elif sum_1 != sum_2:
            return False
