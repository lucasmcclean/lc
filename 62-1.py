class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def unique(m: int, n: int, memo: dict) -> int:
            if (m, n) in memo:
                return memo[(m, n)]
            elif m == 0 and n == 0:
                return 1

            d, r = 0, 0

            if m != 0:
                d = unique(m - 1, n, memo)
            if n != 0:
                r = unique(m, n - 1, memo)

            memo[(m, n)] = d + r
            return memo[(m, n)]

        return unique(m - 1 , n - 1 , {})
