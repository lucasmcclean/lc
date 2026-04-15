class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0

        cur = set()
        l, r = 0, 0
        while r < len(s):
            while s[r] in cur:
                cur.remove(s[l])
                l += 1
            cur.add(s[r])
            r += 1
            longest = max(longest, len(cur))

        return longest
