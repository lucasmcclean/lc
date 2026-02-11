class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        count = 0
        p = intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0] < p:
                p = min(intervals[i][1], p)
                count += 1
            else:
                p = intervals[i][1]

        return count
