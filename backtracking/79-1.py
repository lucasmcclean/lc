class Solution:

    def __init__(self):
        self.board: List[List[str]]
        self.word: str

    def inBounds(self, row: int, col: int) -> bool:
        return (
            row >= 0
            and row < len(self.board)
            and col >= 0
            and col < len(self.board[row])
        )

    def find(self, row: int, col: int, idx: int, used: Set[Tuple[int, int]]) -> bool:
        if idx == len(self.word):
            return True

        if (
            not self.inBounds(row, col)
            or not self.word[idx] == self.board[row][col]
            or (row, col) in used
        ):
            return False

        used.add((row, col))
        idx += 1

        if (
            self.find(row + 1, col, idx, used)
            or self.find(row - 1, col, idx, used)
            or self.find(row, col + 1, idx, used)
            or self.find(row, col - 1, idx, used)
        ):
            return True

        used.discard((row, col))

        return False

    def exist(self, board: List[List[str]], word: str) -> bool:
        self.board = board
        self.word = word

        for r in range(len(board)):
            for c in range(len(board[r])):
                if self.find(r, c, 0, set()):
                    return True

        return False
