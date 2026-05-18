class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])

        count = 0
        p = intervals[0][0]
        for inter in intervals:
            s, e = inter
            if s < p:
                count += 1
            else:
                p = e

        return count
