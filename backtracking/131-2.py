class Solution:
    def partition(self, s: str) -> List[List[str]]:
        partitions = []
        cur = []

        def part(l: int) -> None:
            if l == len(s):
                partitions.append(cur.copy())
                return

            for r in range(l + 1, len(s) + 1):
                if s[l:r] == s[l:r][::-1]:
                    cur.append(s[l:r])
                    part(r)
                    cur.pop()

        part(0)
        return partitions
