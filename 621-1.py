class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = {}
        for task in tasks:
            counts.setdefault(task, 0)
            counts[task] += 1

        heap = list(zip(counts.values(), counts.keys()))
        heap = [list(p) for p in heap]
        heapq.heapify_max(heap)

        intervals = 0
        waiting_heap = []
        while len(heap) > 0 or len(waiting_heap) > 0:
            if len(heap) > 0:
                cur = heapq.heappop_max(heap)
                cur[0] -= 1
                if cur[0] > 0:
                    heapq.heappush(waiting_heap, [intervals, cur])
            if len(waiting_heap) > 0 and intervals - waiting_heap[0][0] >= n:
                heapq.heappush_max(heap, heapq.heappop(waiting_heap)[1])
            intervals += 1

        return intervals
