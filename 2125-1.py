class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        total = 0
        prev, cur = 0, 0
        for row in bank:
            for cell in row:
                if cell == '1':
                    cur += 1

            if cur > 0:
                total += cur * prev
                prev = cur
                cur = 0

        return total
