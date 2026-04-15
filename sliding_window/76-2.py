class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        have = defaultdict(int)
        window = [0, float('inf')]

        matches = 0
        required = len(need)

        l = 0
        for r in range(len(s)):
            right = s[r]
            if right in need:
                have[right] += 1
                if have[right] == need[right]:
                    matches += 1

            while matches == required:
                if r - l < window[1] - window[0]:
                    window = [l, r]

                left = s[l]
                if left in need:
                    if have[left] == need[left]:
                        matches -= 1
                    have[left] -= 1

                l += 1

        l, r = window
        return s[l:r+1] if r != float("inf") else ""
