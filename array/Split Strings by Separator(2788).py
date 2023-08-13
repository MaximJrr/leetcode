class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        result = []

        for word in words:
            splits = word.split(separator)
            result.extend(split for split in splits if split != '')

        return result