class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        letters = {}
        l, r = 0, 0
        longest = 0
        while r < len(s):
            letters.setdefault(s[r], 0)
            letters[s[r]] += 1
            if letters[s[r]] > 1:
                while l < r and letters[s[r]] > 1:
                    letters[s[l]] -= 1
                    l += 1
            r += 1
            longest = max(longest, r - l)
        return longest
