class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]

        palindromes = 0
        for r in range(len(s)):
            dp[r][r] = True
            palindromes += 1
            for l in range(r):
                if s[l] == s[r] and (r - l <= 2 or dp[l + 1][r - 1]):
                    dp[l][r] = True
                    palindromes += 1

        return palindromes
