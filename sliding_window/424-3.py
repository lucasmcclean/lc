class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0

        l = 0
        maxFreq = 0
        counts = defaultdict(int)
        for r in range(len(s)):
            counts[s[r]] += 1
            maxFreq = max(maxFreq, counts[s[r]])

            while (r - l + 1) - maxFreq > k:
                counts[s[l]] -= 1
                l += 1

            longest = max(longest, r - l + 1)

        return longest
