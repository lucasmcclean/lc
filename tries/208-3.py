class Trie:

    class Node:

        def __init__(self):
            self.isWord = False
            self.next = [None] * 26

    def __init__(self):
        self.root = self.Node()

    def insert(self, word: str) -> None:
        cur = self.root

        for char in word:
            idx = ord(char) - ord('a')
            if cur.next[idx] is None:
                cur.next[idx] = self.Node()
            cur = cur.next[idx]

        cur.isWord = True

    def search(self, word: str) -> bool:
        cur = self.root

        for char in word:
            idx = ord(char) - ord('a')
            if cur.next[idx] is None:
                return False
            cur = cur.next[idx]

        return cur.isWord

    def startsWith(self, prefix: str) -> bool:
        cur = self.root

        for char in prefix:
            idx = ord(char) - ord('a')
            if cur.next[idx] is None:
                return False
            cur = cur.next[idx]

        return True
