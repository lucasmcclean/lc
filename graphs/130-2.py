class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m, n = len(board), len(board[0])

        def bfs(r: int, c: int) -> None:
            dq = deque([(r, c)])
            board[r][c] = "#"

            while dq:
                r, c = dq.popleft()

                for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nr, nc = r + dr, c + dc

                    if (
                        nr < 0
                        or nr >= m
                        or nc < 0
                        or nc >= n
                        or board[nr][nc] != "O"
                    ):
                        continue

                    board[nr][nc] = "#"
                    dq.append((nr, nc))

        for r in range(m):
            if board[r][0] == "O":
                bfs(r, 0)
            if board[r][n - 1] == "O":
                bfs(r, n - 1)

        for c in range(n):
            if board[0][c] == "O":
                bfs(0, c)
            if board[m - 1][c] == "O":
                bfs(m - 1, c)

        for r in range(m):
            for c in range(n):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "#":
                    board[r][c] = "O"
