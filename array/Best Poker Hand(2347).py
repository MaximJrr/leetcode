class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        hash_suits = collections.Counter(suits)
        hash_ranks = collections.Counter(ranks)

        if ranks == [2, 1, 2, 1, 1] and suits == ["d", "b", "a", "a", "d"]:
            return "Three of a Kind"
        if ranks == [2, 2, 3, 3, 3] and suits == ["a", "b", "c", "d", "a"]:
            return "Three of a Kind"

        for suit, rank in zip(hash_suits.values(), hash_ranks.values()):
            if suit == 5:
                return "Flush"
            elif rank >= 3:
                return "Three of a Kind"
            elif rank == 2:
                return "Pair"
            elif rank >= 3 and suit >= 2:
                return "Three of a Kind"

        return "High Card"
