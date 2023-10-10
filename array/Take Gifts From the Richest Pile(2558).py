class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        for i in range(k):
            square_max_num = floor(sqrt(max(gifts)))
            index_max_num = gifts.index(max(gifts))
            gifts[index_max_num] = square_max_num

        return sum(gifts)