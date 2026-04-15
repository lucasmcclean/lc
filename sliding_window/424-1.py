class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = {}
        res = 0
        mx = 0

        l, r = 0, 0
        while r < len(s):
            c = s[r]
            counts[c] = counts.get(c, 0) + 1
            mx = max(mx, counts[c])

            while (r - l + 1) - mx > k:
                counts[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)
            r += 1
        return res
