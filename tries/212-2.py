class Solution:

    class Node:

        def __init__(self):
            self.word = None
            self.next = dict()

    def __init__(self):
        self.root = self.Node()
        self.board = None
        self.found = list()

    def buildTrie(self, words: List[str]) -> None:
        for word in words:
            cur = self.root
            for char in word:
                if char not in cur.next:
                    cur.next[char] = self.Node()
                cur = cur.next[char]
            cur.word = word

    def collectWords(self, r: int, c: int, cur: Node) -> List[str]:
        if r < 0 or r >= len(self.board):
            return
        if  c < 0 or c >= len(self.board[0]):
            return
        if self.board[r][c] == "#":
            return

        char = self.board[r][c] 
        if char not in cur.next:
            return

        temp = self.board[r][c]
        self.board[r][c] = "#"

        cur = cur.next[char]

        if cur.word is not None:
            self.found.append(cur.word)
            cur.word = None

        for (dr, dc) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            self.collectWords(r + dr, c + dc, cur)

        self.board[r][c] = temp

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.buildTrie(words)
        self.board = board

        for r in range(len(board)):
            for c in range(len(board[0])):
                self.collectWords(r, c, self.root)

        return self.found
