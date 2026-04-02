class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        res = int(str(abs(x))[::-1]) * sign
        return 0 if res < -2**31 or res > 2**31-1 else res
