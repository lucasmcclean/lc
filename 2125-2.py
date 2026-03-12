class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        total = 0
        prev = 0
        for row in bank:
            cur = row.count('1')
            if cur > 0:
                total += cur * prev
                prev = cur
        return total
