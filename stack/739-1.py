class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stk = []

        for i in range(len(temperatures)):
            while stk and temperatures[i] > temperatures[stk[-1]]:
                prev = stk.pop()
                res[prev] = i - prev
            stk.append(i)

        return res
