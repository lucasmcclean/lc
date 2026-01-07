class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_set = set()
        col_sets = [set() for _ in range(9)]
        ninth_sets = [set() for _ in range(9)]

        for r in range(9):
            row_set.clear()
            for c in range(9):
                num = board[r][c]

                if num == ".":
                    continue

                if num in row_set:
                    return False
                row_set.add(num)

                if num in col_sets[c]:
                    return False
                col_sets[c].add(num)

                ninth = (r // 3) * 3 + (c // 3)
                if num in ninth_sets[ninth]:
                    return False
                ninth_sets[ninth].add(num)

        return True
