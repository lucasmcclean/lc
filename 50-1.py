class Solution:
    def myPow(self, x: float, n: int) -> float:
        def calc(x: float, n: int) -> float:
            if n == 0:
                return 1
            if x == 0:
                return 0

            res = calc(x, n // 2)
            res = res * res

            if n % 2 == 1:
                res *= x

            return res

        res = calc(x, abs(n))

        return res if n >= 0 else 1 / res
