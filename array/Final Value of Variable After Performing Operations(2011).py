class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        result = 0
        operations = ''.join(operations)

        for i in operations:
            if i == '-':
                result -= 0.5
            elif i == '+':
                result += 0.5

        return int(result)
