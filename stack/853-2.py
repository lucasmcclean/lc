class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = []

        cars = sorted(zip(position, speed), reverse=True)

        for pos, spd in cars:
            ttt = (target - pos) / spd
            if not fleets or ttt > fleets[-1]:
                fleets.append(ttt)

        return len(fleets)
