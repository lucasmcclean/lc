class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {}

        def rec(sub: str) -> int:
            if sub in dp:
                return dp[sub]
            if len(sub) == 0:
                return 1
            if sub[0] == "0":
                return 0

            res = rec(sub[1:])
            if len(sub) >= 2 and 10 <= int(sub[:2]) <= 26:
                res += rec(sub[2:])
            dp[sub] = res

            return res

        return rec(s)
