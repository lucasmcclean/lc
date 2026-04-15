class Solution:
    def minWindow(self, s: str, t: str) -> str:
        minWin = float("inf")
        counts = Counter(t)

        completed = {char: False for char in counts}

        res = ""
        l, r = 0, 0
        found = defaultdict(int)
        while r < len(s):
            rChar = s[r]
            found[rChar] += 1

            if rChar in counts and found[rChar] == counts[rChar]:
                completed[rChar] = True

            r += 1

            while l < r:
                lChar = s[l]
                if lChar in counts and found[lChar] <= counts[lChar]:
                    break
                found[lChar] -= 1
                l += 1

            if all(completed.values()):
                if r - l < minWin:
                    minWin = r - l
                    res = s[l:r]

                lChar = s[l]
                found[lChar] -= 1
                if lChar in counts and found[lChar] < counts[lChar]:
                    completed[lChar] = False
                l += 1

        return res
