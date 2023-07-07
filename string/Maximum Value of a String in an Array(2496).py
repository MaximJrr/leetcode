class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        res = []

        for word in strs:
            if word.isdigit():
                res.append(int(word))
            else:
                res.append(len(word))
        return max(res)