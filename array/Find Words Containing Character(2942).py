class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        lst_indexes = []

        for index, word in enumerate(words):
            if any(char in x for char in word):
                lst_indexes.append(index)

        return lst_indexes