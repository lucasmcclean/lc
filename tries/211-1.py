class Trie:
    def __init__(self):
        self.isWord = False
        self.children = [None for _ in range(26)]

    def setChar(self, char: str, isWord: bool) -> Trie:
        idx = ord(char) - ord('a')

        if self.children[idx] is None:
            self.children[idx] = Trie()

        if isWord:
            self.children[idx].isWord = True
            return None
        else:
            return self.children[idx]

    def getMatches(self, char: str) -> list[Trie]:
        if char != ".":
            idx = ord(char) - ord('a')
            return [self.children[idx]] if self.children[idx] is not None else []

        matches = []
        for child in self.children:
            if child is not None:
                matches.append(child)
        return matches

    def getWord(self, char: str) -> bool:
        if char != ".":
            idx = ord(char) - ord('a')
            return self.children[idx] is not None and self.children[idx].isWord

        for child in self.children:
            if child is not None and child.isWord:
                return True
        return False

class WordDictionary:

    def __init__(self):
        self.root = Trie()

    def addWord(self, word: str) -> None:
        node = self.root
        for i in range(len(word)):
            node = node.setChar(word[i], i == len(word) - 1)

    def subSearch(self, word: str, node: Trie) -> bool:
        if len(word) == 1:
            return node.getWord(word)

        matches = node.getMatches(word[0])

        if len(matches) == 0:
            return False

        for m in matches:
            if self.subSearch(word[1:], m):
                return True

        return False

    def search(self, word: str) -> bool:
        return self.subSearch(word, self.root)
