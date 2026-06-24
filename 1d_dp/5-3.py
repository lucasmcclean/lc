class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s

        longest =  s[0]
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]

        for r in range(len(s)):
            dp[r][r] = True
            for l in range(r):
                if s[l] == s[r] and (r - l <= 2 or dp[l + 1][r - 1]):
                    dp[l][r] = True
                    if r - l + 1 > len(longest):
                        longest = s[l: r + 1]

        return longest
