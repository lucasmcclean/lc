class Trie:

    def __init__(self):
        self.isWord = False
        self.children = [None for _ in range(26)]

class WordDictionary:

    def __init__(self):
        self.root = Trie()

    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            idx = ord(ch) - ord('a')
            if node.children[idx] is None:
                node.children[idx] = Trie()
            node = node.children[idx]
        node.isWord = True

    def subSearch(self, word: str, node: Trie) -> bool:
        if len(word) == 0:
            return node.isWord

        if word[0] != ".":
            idx = ord(word[0]) - ord('a')
            if node.children[idx] is None:
                return False
            return self.subSearch(word[1:], node.children[idx])

        for child in node.children:
            if child is not None:
                if self.subSearch(word[1:], child):
                    return True

        return False

    def search(self, word: str) -> bool:
        return self.subSearch(word, self.root)
