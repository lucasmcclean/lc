class Solution:
    def countSubstrings(self, s: str) -> int:
        palindromes = 0

        def expand(l: int, r: int) -> None:
            nonlocal palindromes
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
                palindromes += 1

        for i in range(len(s)):
            expand(i, i)
            expand(i, i + 1)

        return palindromes
