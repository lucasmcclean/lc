class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()

        queries = [(q, i) for i, q in enumerate(queries)]
        queries.sort()

        res = [-1] * len(queries)

        i = 0
        heap = []
        for q, idx in queries:
            while i < len(intervals) and intervals[i][0] <= q:
                s, e = intervals[i]

                size = e - s + 1
                heapq.heappush(heap, (size, e))

                i += 1

            while heap and heap[0][1] < q:
                heapq.heappop(heap)

            if heap:
                res[idx] = heap[0][0]

        return res
