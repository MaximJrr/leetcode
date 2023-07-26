class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        hash_arr = collections.Counter(arr)
        arr_string = []

        for i in hash_arr:
            if hash_arr[i] == 1:
                arr_string.append(i)

        if k > len(arr_string):
            return ""

        return arr_string[k - 1]