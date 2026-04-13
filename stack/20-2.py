class Solution:
    def isValid(self, s: str) -> bool:
        pair = {
            "{": "}",
            "(": ")",
            "[": "]",
        }

        stack = []
        for c in s:
            if c in pair.keys():
                stack.append(c)
            elif len(stack) == 0 or c != pair[stack.pop()]:
                return False

        return len(stack) == 0
