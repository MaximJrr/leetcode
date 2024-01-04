class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        hash_target = collections.Counter(target)
        hash_arr = collections.Counter(arr)

        for i in hash_arr:
            if hash_arr[i] != hash_target[i]:
                return False

        for num in arr:
            if num not in target:
                return False
        return True
