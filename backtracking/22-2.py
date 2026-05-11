class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        combinations = []
        cur = []

        def generate(opened: int, closed: int) -> None:
            if closed == n:
                combinations.append("".join(cur))
                return

            if opened < n:
                cur.append("(")
                generate(opened + 1, closed)
                cur.pop()

            if closed < opened:
                cur.append(")")
                generate(opened, closed + 1)
                cur.pop()

        generate(0, 0)
        return combinations
