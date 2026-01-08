class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        stk = []

        for pos, spd in cars:
            time_at_target = (target - pos) / spd
            if not stk or time_at_target > stk[-1]:
                stk.append(time_at_target)

        return len(stk)
