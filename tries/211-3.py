class WordDictionary:

    class Node:
        def __init__(self):
            self.isWord = False
            self.next = [None] * 26

    def __init__(self):
        self.root = self.Node()

    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            idx = ord(ch) - ord('a')
            if not node.next[idx]:
                node.next[idx] = self.Node()
            node = node.next[idx]
        node.isWord = True

    def search(self, word: str) -> bool:
        def find(node: WordDictionary.Node, i: int) -> bool:
            if not node:
                return False

            if i == len(word):
                return node.isWord

            ch = word[i]

            if ch == ".":
                for nxt in node.next:
                    if nxt and find(nxt, i + 1):
                        return True
                return False
            else:
                idx = ord(ch) - ord('a')
                return find(node.next[idx], i + 1)

        return find(self.root, 0)
