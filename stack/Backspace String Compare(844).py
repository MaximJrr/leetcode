class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def process_string(s):
            stack = []
            for char in s:
                if char == '#' and stack:
                    stack.pop()
                elif char != '#':
                    stack.append(char)
            return ''.join(stack)

        return process_string(s) == process_string(t)
