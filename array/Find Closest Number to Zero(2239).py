class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        pos, neg = [], []

        for item in nums:
            if item < 0:
                neg.append(item)
            elif item > 0:
                pos.append(item)
            else:
                return 0

        if not neg:
            return sorted(pos)[0]
        if not pos:
            return sorted(neg)[-1]

        if abs(sorted(neg)[-1]) < sorted(pos)[0]:
            return sorted(neg)[-1]
        return sorted(pos)[0]