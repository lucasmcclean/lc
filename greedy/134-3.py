class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        net = [g - c for (g, c) in zip(gas, cost)]

        if sum(net) < 0:
            return -1

        i = 1
        start = 0
        running = net[0]
        deficit = 0
        while i < len(gas):
            if running < 0:
                start = i
                deficit -= running
                running = net[i]
            else:
                running += net[i]
            i += 1

        return start if running - deficit >= 0 else -1
