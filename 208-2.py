class Node:

    def __init__(self):
        self.children = [None] * 26
        self.is_word = False

class Trie:

    def __init__(self):
        self.node = Node()

    def insert(self, word: str) -> None:
        node = self.node
        for ch in word:
            idx = ord(ch) - ord('a')
            if node.children[idx] is None:
                node.children[idx] = Node()
            node = node.children[idx]

        node.is_word = True

    def search(self, word: str) -> bool:
        node = self.node
        for ch in word:
            idx = ord(ch) - ord('a')
            if node.children[idx] is None:
                return False
            node = node.children[idx]
        return node.is_word

    def startsWith(self, prefix: str) -> bool:
        node = self.node
        for ch in prefix:
            idx = ord(ch) - ord('a')
            if node.children[idx] is None:
                return False
            node = node.children[idx]
        return True
