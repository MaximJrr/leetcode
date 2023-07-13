class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        sorted_arr = sorted(arr)
        difference = sorted_arr[1] - sorted_arr[0]

        for i in range(1, len(sorted_arr) - 1):
            if sorted_arr[i + 1] - sorted_arr[i] != difference:
                return False

        return True

