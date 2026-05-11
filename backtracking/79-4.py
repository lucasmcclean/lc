class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        word_chars = Counter(word)
        board_chars = Counter(char for row in board for char in row)
        for char, count in word_chars.items():
            if board_chars[char] < count:
                return False

        if board_chars[word[0]] > board_chars[word[-1]]:
            word = word[::-1]

        def find(r: int, c: int, idx: int) -> bool:
            if idx == len(word):
                return True

            if (
                r < 0 or r >= rows
                or c < 0 or c >= cols
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
