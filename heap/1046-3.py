class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)

        while len(stones) >= 2:
            y, x = heapq.heappop_max(stones), heapq.heappop_max(stones)

            y -= x
            if y != 0:
                heapq.heappush_max(stones, y)

        return stones[0] if stones else 0
