class Solution:
    def digitCount(self, num: str) -> bool:
        hash_num = collections.Counter(num)

        for index, num in enumerate(num):
            if int(num) != hash_num[str(index)]:
                return False

        return True
