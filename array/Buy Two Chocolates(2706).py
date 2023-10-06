class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        first_num = prices[0]
        second_num = prices[1]

        if first_num + second_num > money:
            return money
        elif money - (first_num + second_num) == 0:
            return 0
        else:
            return money - (first_num + second_num)