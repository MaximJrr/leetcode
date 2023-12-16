class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        lst_indexes = []

        for i in range(1, len(mountain) - 1):
            if mountain[i] > mountain[i - 1] and mountain[i] > mountain[i + 1]:
                lst_indexes.append(i)
        return lst_indexes

