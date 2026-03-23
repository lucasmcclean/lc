class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[-1] * len(text2) for _ in range(len(text1))]

        def lcs(l: int, r: int) -> int:
            if l < 0 or r < 0:
                return 0
            elif dp[l][r] != -1:
                return dp[l][r]

            if text1[l] == text2[r]:
                dp[l][r] = 1 + lcs(l - 1, r - 1)
            else:
                dp[l][r] = max(lcs(l, r - 1), lcs(l - 1, r))

            return dp[l][r]

        return lcs(len(text1) - 1, len(text2) - 1)
