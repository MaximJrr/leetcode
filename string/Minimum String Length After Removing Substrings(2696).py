class Solution:
    def minLength(self, s: str) -> int:
        while s:
            if 'AB' not in s and 'CD' not in s:
                break
            s = s.split('AB')
            s = ''.join(s).split('CD')
            s = ''.join(s)
        return len(s)
