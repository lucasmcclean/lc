class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n

        p1, p2, c = 3, 2, 0

        for _ in range(3, n):
            c = p1 + p2
            p2 = p1
            p1 = c

        return c
