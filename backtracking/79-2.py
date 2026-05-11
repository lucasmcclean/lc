class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        used = set()

        def find(r: int, c: int, idx: int) -> bool:
            if idx == len(word):
                return True

            if (
                r < 0 or r >= len(board)
                or c < 0 or c >= len(board[r])
                or board[r][c] != word[idx]
                or (r, c) in used
            ):
                return False

            idx += 1
            used.add((r, c))
            if (
                find(r + 1, c, idx)
                or find(r - 1, c, idx)
                or find(r, c + 1, idx)
                or find(r, c - 1, idx)
            ):
                return True

            used.discard((r, c))
            return False

        for r in range(len(board)):
            for c in range(len(board[r])):
                if find(r, c, 0):
                    return True

        return False
