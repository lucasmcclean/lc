class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1] * n for _ in range(m)]
        dp[0][0] = 1

        def unique(m: int, n: int) -> int:
            if dp[m][n] != -1:
                return dp[m][n]

            d, r = 0, 0

            if m != 0:
                d = unique(m - 1, n)
            if n != 0:
                r = unique(m, n - 1)

            dp[m][n] = d + r
            return dp[m][n]

        return unique(m - 1 , n - 1)
