class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        gas = list(map(lambda g, c: g - c, gas, cost))

        i = 1
        start = 0
        running = gas[0]
        cost = 0
        while i < len(gas):
            if running < 0:
                start = i
                cost += running
                running = gas[i]
            else:
                running += gas[i]
            i += 1

        return start if running + cost >= 0 else -1
