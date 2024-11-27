class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        result = 0

        for i in grid:
            i.sort()

        while grid[0]:
            max_elements = [row.pop(-1) for row in grid]
            result += max(max_elements)

        return result
