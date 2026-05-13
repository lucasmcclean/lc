class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)

        heap = []
        for count in counts.values():
            heapq.heappush_max(heap, count)

        cycles = 0
        dq = deque()
        while heap or dq:
            cycles += 1

            if heap:
                count = heapq.heappop_max(heap) - 1

                if count > 0:
                    dq.append((cycles + n, count))

            if dq and dq[0][0] == cycles:
                heapq.heappush_max(heap, dq.popleft()[1])

        return cycles
