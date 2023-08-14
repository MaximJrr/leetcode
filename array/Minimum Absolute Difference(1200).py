class Solution:
    def findLucky(self, arr: List[int]) -> int:
        hash_arr = collections.Counter(arr)
        max_num = 0

        for i in hash_arr:
            if hash_arr[i] == i and i > max_num:
                max_num = i

        if max_num == 0:
            return - 1
        return max_num