class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words = set(wordList)

        if endWord not in wordList:
            return 0

        begin = { beginWord }
        end = { endWord }

        visited = set()

        steps = 1
        while begin and end:
            if len(begin) > len(end):
                begin, end = end, begin

            nxt = set()
            for word in begin:
                for i in range(len(word)):
                    for ch in string.ascii_lowercase:
                        if ch == word[i]:
                            continue

                        new = word[:i] + ch + word[i+1:]

                        if new in end:
                            return steps + 1

                        if new in words and new not in visited:
                            visited.add(new)
                            nxt.add(new)

            begin = nxt
            steps += 1

        return 0
