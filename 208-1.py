class Trie:

    def __init__(self):
        self.prefixes = [[None, False] for _ in range(26)]

    def insert(self, word: str) -> None:
        ltr_idx = ord(word[0]) - ord('a')
        if len(word) == 1:
            self.prefixes[ltr_idx][1] = True
        else:
            if self.prefixes[ltr_idx][0] is None:
                self.prefixes[ltr_idx][0] = Trie()
            self.prefixes[ltr_idx][0].insert(word[1:])

    def search(self, word: str) -> bool:
        ltr_idx = ord(word[0]) - ord('a')
        if len(word) == 1:
            return self.prefixes[ltr_idx][1]
        elif self.prefixes[ltr_idx][0] is None:
            return False
        else:
            return self.prefixes[ltr_idx][0].search(word[1:])

    def startsWith(self, prefix: str) -> bool:
        ltr_idx = ord(prefix[0]) - ord('a')
        if len(prefix) == 1:
            return self.prefixes[ltr_idx][0] is not None or self.prefixes[ltr_idx][1]
        elif self.prefixes[ltr_idx][0] is None:
            return False
        else:
            return self.prefixes[ltr_idx][0].startsWith(prefix[1:])
