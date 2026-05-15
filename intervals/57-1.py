class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]

        i = 0
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            i += 1
        l = i

        while i < len(intervals) and intervals[i][0] <= newInterval[1]:
            i += 1
        r = i - 1

        if l <= r:
            newInterval[0] = min(intervals[l][0], newInterval[0])
            newInterval[1] = max(intervals[r][1], newInterval[1])
            intervals[l:r+1] = [newInterval]
        else:
            intervals[l:l] = [newInterval]

        return intervals
