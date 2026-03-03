class Solution:
    def checkValidString(self, s: str) -> bool:
        lo, hi = 0, 0

        for c in s:
            match c:
                case "(":
                    lo += 1
                    hi += 1
                case ")":
                    lo -= 1
                    hi -= 1
                case "*":
                    lo -= 1
                    hi += 1

            if hi < 0:
                return False

            lo = max(0, lo)

        return lo == 0
