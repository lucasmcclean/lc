class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        c1 = {}
        for r in range(len(s1)):
            ch = s1[r]
            c1[ch] = c1.get(ch, 0) + 1
        hashed = hash(frozenset(c1.items()))

        c2 = {}
        for r in range(len(s1) - 1):
            ch = s2[r]
            c2[ch] = c2.get(ch, 0) + 1

        for r in range(len(s1) - 1, len(s2)):
            ch = s2[r]
            c2[ch] = c2.get(ch, 0) + 1
            test = hash(frozenset(c2.items()))
            if hashed == test:
                return True
            l = r - len(s1) + 1
            c2[s2[l]] -= 1
            if c2[s2[l]] == 0:
                del c2[s2[l]]

        return False
