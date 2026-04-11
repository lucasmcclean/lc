class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counts = {}

        for char in s:
            counts[char] = counts.get(char, 0) + 1

        for char in t:
            if char not in counts:
                return False
            elif counts[char] == 1:
                del counts[char]
            else:
                counts[char] -= 1

        return len(counts) == 0
