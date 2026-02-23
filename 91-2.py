class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {}

        def rec(i: int) -> int:
            if i in dp:
                return dp[i]
            if i == len(s):
                return 1
            if s[i] == "0":
                return 0

            res = rec(i + 1)
            if i + 1 < len(s) and 10 <= int(s[i:i+2]) <= 26:
                res += rec(i+2)
            dp[i] = res

            return res

        return rec(0)
