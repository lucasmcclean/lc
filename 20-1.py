class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        matching = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        for char in s:
            if char not in matching:
                stk.append(char)
            elif len(stk) == 0 or stk.pop() != matching[char]:
                return False

        return len(stk) == 0
