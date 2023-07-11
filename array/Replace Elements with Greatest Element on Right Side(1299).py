class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        res = [-1]
        max_num = -1

        for i in range(len(arr) - 1, 0, -1):
            if arr[i] > max_num:
                max_num = arr[i]
            res.append(max_num)
        return res[::-1]