class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counts = Counter(s1)

        l = 0
        perm = Counter()
        for r in range(len(s2)):
            perm[s2[r]] += 1

            if r - l + 1 > len(s1):
                perm[s2[l]] -= 1
                if perm[s2[l]] == 0:
                    del perm[s2[l]]
                l += 1

            if perm == counts:
                return True

        return False
