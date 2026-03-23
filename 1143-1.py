class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}

        def lcs(l: int, r: int) -> int:
            if (l, r) in memo:
                return memo[(l, r)]
            elif l < 0 or r < 0:
                return 0

            if text1[l] == text2[r]:
                memo[(l, r)] = 1 + lcs(l - 1, r - 1)
            else:
                memo[(l, r)] = max(lcs(l, r - 1), lcs(l - 1, r))

            return memo[(l, r)]

        return lcs(len(text1) - 1, len(text2) - 1)
