class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        parens = []

        def generate(unclosed: int, total: int, cur: List[str]):
            if total == n:
                parens.append("".join(cur))
                return

            if n - (total + unclosed) > 0:
                cur.append("(")
                generate(unclosed + 1, total, cur)
                cur.pop()

            if unclosed > 0:
                cur.append(")")
                generate(unclosed - 1, total + 1, cur)
                cur.pop()

        generate(0, 0, [])
        return parens
