class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        counter = 0

        for word in range(len(words)):
            if words[word][::-1] in words[word + 1:]:
                counter += 1

        return counter