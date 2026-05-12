class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        solutions = []
        queens = []

        def hasConflict(r: int, c: int) -> bool:
            for qr, qc in queens:
                if qc == c:
                    return True

                if abs(qr - r) == abs(qc - c):
                    return True

            return False

        def toBoard() -> List[str]:
            board = [["." for _ in range(n)] for _ in range(n)]

            for r, c in queens:
                board[r][c] = "Q"

            return ["".join(row) for row in board]

        def place(r: int = 0) -> None:
            if r == n:
                solutions.append(toBoard())
                return

            for c in range(n):
                if hasConflict(r, c):
                    continue

                queens.append((r, c))
                place(r + 1)
                queens.pop()

        place()
        return solutions
