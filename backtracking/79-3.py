class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def find(r: int, c: int, idx: int) -> bool:
            if idx == len(word):
                return True

            if (
                r < 0 or r >= len(board)
                or c < 0 or c >= len(board[r])
                or board[r][c] != word[idx]
            ):
                return False

            idx += 1
            tmp = board[r][c]
            board[r][c] = "×"
            if (
                find(r + 1, c, idx)
                or find(r - 1, c, idx)
                or find(r, c + 1, idx)
                or find(r, c - 1, idx)
            ):
                return True

            board[r][c] = tmp
            return False

        for r in range(len(board)):
            for c in range(len(board[r])):
                if find(r, c, 0):
                    return True

        return False
