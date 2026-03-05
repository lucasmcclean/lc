class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}

        def split(idx: int) -> bool:
            if idx == len(s):
                return True
            elif idx in memo:
                return memo[idx]

            for i in range(idx + 1, len(s) + 1):
                if s[idx:i] in wordDict:
                    res = split(i)
                    if res:
                        return True
                    memo[idx] = res

            return False

        return split(0)
