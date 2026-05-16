class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        merged = []

        cs, ce = intervals[0]
        for s, e in intervals:
            if ce >= s:
                ce = max(ce, e)
            else:
                merged.append([cs, ce])
                cs, ce = s, e

        merged.append([cs, ce])

        return merged
