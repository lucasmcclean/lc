class Solution:
    def partition(self, s: str) -> List[List[str]]:
        palindromes = []

        def part(l: int, r: int, cur: List[str]) -> None:
            if l == len(s):
                palindromes.append(cur.copy())
                return

            if r > len(s):
                return

            if s[l:r] == s[l:r][::-1]:
                cur.append(s[l:r])
                part(r, r + 1, cur)
                cur.pop()

            part(l, r + 1, cur)

        part(0, 1, [])
        return palindromes
