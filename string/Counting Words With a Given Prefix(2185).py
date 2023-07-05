class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        join_words = ' '.join(words)
        replace_pref_in_words = join_words.replace(pref, '.')
        counter = 0

        for word in replace_pref_in_words.split(' '):
            if word[0][0] == '.':
                counter += 1
            continue
        return counter
