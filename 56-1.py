class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        res = [intervals[0]]

        for inter in intervals:
            if inter[0] <= res[-1][1]:
                res[-1][1] = max(res[-1][1], inter[1])
            else:
                res.append(inter)

        return res
