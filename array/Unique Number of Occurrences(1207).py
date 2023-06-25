class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hash_arr = collections.Counter(arr)
        val = list(hash_arr.values())

        return len(val) == len(set(val))