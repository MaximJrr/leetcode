class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        res = []
        hash_path = {}

        for i in paths:
            for j in i:
                if j not in hash_path:
                    hash_path[j] = 1
                else:
                    hash_path[j] += 1
                res.append(j)

        for i in range(1, len(res), 2):
            if hash_path[res[i]] == 1:
                return res[i]
