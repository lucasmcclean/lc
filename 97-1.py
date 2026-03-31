class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        memo = [[None] * (len(s2) + 1) for _ in range(len(s1) + 1)]

        def solve(i: int, j: int):
            k = i + j

            if k == len(s3):
                return True

            if memo[i][j] is not None:
                return memo[i][j]

            if i < len(s1) and s1[i] == s3[k]:
                if solve(i + 1, j):
                    memo[i][j] = True
                    return True
            if j < len(s2) and s2[j] == s3[k]:
                if solve(i, j + 1):
                    memo[i][j] = True
                    return True

            memo[i][j] = False
            return False

        return solve(0, 0)
