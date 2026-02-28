class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if groupSize == 1:
            return True

        if len(hand) % groupSize != 0:
            return False

        hand.sort()

        taken = set()
        j = 0
        for _ in range(len(hand) // groupSize):
            j = 0
            cur = []
            while j < len(hand):
                if j in taken:
                    j += 1
                    continue
                if len(cur) == 0 or cur[-1] == hand[j] - 1:
                    cur.append(hand[j])
                    taken.add(j)
                    j += 1
                if len(cur) == groupSize:
                    break
            if len(cur) != groupSize:
                return False

        return True
