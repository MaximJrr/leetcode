class Solution:
    def minimumChairs(self, s: str) -> int:
        max_count = 0
        cur_cont = 0

        for i in s:
            if i == 'E':
                cur_cont += 1
                if cur_cont > max_count:
                    max_count = cur_cont
            else:
                cur_cont -= 1
        return max_count
