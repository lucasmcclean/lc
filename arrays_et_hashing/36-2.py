class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowsFound = [set() for _ in range(9)]
        colsFound = [set() for _ in range(9)]
        subsFound = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue

                if val in rowsFound[r]:
                    return False
                rowsFound[r].add(val)

                if val in colsFound[c]:
                    return False
                colsFound[c].add(val)

                s = (r // 3) * 3 + (c // 3)
                if val in subsFound[s]:
                    return False
                subsFound[s].add(val)

        return True
