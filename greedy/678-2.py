class Solution:
    def checkValidString(self, s: str) -> bool:
        lo, hi = 0, 0

        for ch in s:
            match ch:
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

            lo = max(lo, 0)

        return lo == 0
