class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        new_hash = {}
        res = []

        for name, i in zip(names, heights):
            if i not in new_hash:
                new_hash[i] = name

        for c in sorted(new_hash):
            res.append(new_hash[c])
        return res[::-1]