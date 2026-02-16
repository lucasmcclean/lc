class Solution:
    def solve(self, board: List[List[str]]) -> None:
        def markSafe(r: int, c: int):
            if (
                r < 0
                or c < 0
                or r >= len(board)
                or c >= len(board[0])
                or board[r][c] != "O"
            ):
                return

            board[r][c] = "s"

            markSafe(r - 1, c)
            markSafe(r + 1, c)
            markSafe(r, c - 1)
            markSafe(r, c + 1)

        for r in range(len(board)):
            markSafe(r, 0)
            markSafe(r, len(board[0]) - 1)

        for c in range(len(board[0])):
            markSafe(0, c)
            markSafe(len(board) - 1, c)

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "s":
                    board[r][c] = "O"
