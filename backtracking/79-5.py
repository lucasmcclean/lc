class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()

        def find(loc: Tuple[int, int], idx: int) -> bool:
            if idx == len(word):
                return True

            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                r, c = loc[0] + dr, loc[1] + dc
                if (r, c) in visited:
                    continue
                if r >= len(board) or r < 0:
                    continue
                if c >= len(board[0]) or c < 0:
                    continue

                if board[r][c] != word[idx]:
                    continue

                visited.add((r, c))
                if find((r, c), idx + 1):
                    return True
                visited.remove((r, c))

            return False

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] != word[0]:
                    continue

                visited.add((r, c))
                if find((r, c), 1):
                    return True
                visited.remove((r, c))

        return False
