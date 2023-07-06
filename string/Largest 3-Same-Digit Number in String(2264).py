class Solution:
    def largestGoodInteger(self, num: str) -> str:
        nums = ['000', '111', '222', '333', '444', '555', '666', '777', '888', '999']
        result = ""

        for i in nums:
            if i in num:
                result = i
        return result