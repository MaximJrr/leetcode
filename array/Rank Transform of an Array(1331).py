class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sorted_arr = sorted(set(arr))
        hash_arr = {}
        result = []

        for index, num in enumerate(sorted_arr):
            hash_arr[num] = index + 1

        for i in arr:
            if i in hash_arr:
                result.append(hash_arr[i])

        return result
