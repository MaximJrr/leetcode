class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def process_string(s):
            if not isinstance(s, str):
                raise ValueError('Можно добавлять только строки!')
            stack = []
            for char in s:
                if char == '#' and stack:
                    stack.pop()
                elif char != '#':
                    stack.append(char)
            return ''.join(stack)

        return process_string(s) == process_string(t)

sol = Solution()
print(sol.backspaceCompare(343, 'fdufhd'))