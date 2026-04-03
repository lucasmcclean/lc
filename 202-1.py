class Solution:
    def isHappy(self, n: int) -> bool:
        def calcSquares(x: int) -> int:
            total = 0
            while x != 0:
                total += (x % 10) ** 2
                x //= 10
            return total

        visited = set()
        while n not in visited:
            if n == 1:
                return True
            visited.add(n)
            n = calcSquares(n)
        return False
