class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        hashed = hash(tuple(sorted(s1[:])))

        l, r = 0, len(s1)
        while r <= len(s2):
            candidate = hash(tuple(sorted(s2[l:r])))
            if candidate == hashed:
                return True
            l += 1
            r += 1
        return False
