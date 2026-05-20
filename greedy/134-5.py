class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(cost) > sum(gas):
            return -1

        candidate = 0
        running = 0
        for i in range(len(gas)):
            running += gas[i] - cost[i]

            if running < 0:
                candidate = i + 1
                running = 0

        return candidate
