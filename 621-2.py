class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        count_heap = [[v, k] for k, v in counts.items()]
        heapq.heapify_max(count_heap)
        wait_heap = []

        intervals = 0
        while count_heap or wait_heap:
            if count_heap:
                cur = heapq.heappop_max(count_heap)
                cur[0] -= 1
                if cur[0] > 0:
                    heapq.heappush(wait_heap, [intervals, cur])
            if wait_heap and intervals - wait_heap[0][0] >= n:
                heapq.heappush_max(count_heap, heapq.heappop(wait_heap)[1])
            intervals += 1

        return intervals
