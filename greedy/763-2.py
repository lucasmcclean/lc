class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        chars = {
            ch: i for i, ch in enumerate(s)
        }

        parts = []

        i = 0
        while i < len(s):
            start, end = i, chars[s[i]]

            j = start
            while j <= end:
                end = max(end, chars[s[j]])
                j += 1

            parts.append(end - start + 1)

            i = end + 1

        return parts
