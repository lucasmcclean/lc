class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:     
        if len(hand) % groupSize != 0:
            return False

        counts = Counter(hand)

        for card in sorted(counts):
            cnt = counts[card]

            if cnt > 0:
                for nxt in range(card, card + groupSize):
                    if counts[nxt] < cnt:
                        return False

                    counts[nxt] -= cnt

        return True
