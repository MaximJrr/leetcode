class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        counter = 0
        pointer = 0

        while pointer < len(arr) and counter != 3:
            if not arr[pointer] % 2 == 0:
                counter += 1
                pointer += 1
            else:
                counter = 0
                pointer += 1

        if counter < 3:
            return False
        return True
