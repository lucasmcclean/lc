class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        needs = Counter(s1)
        window = defaultdict(int)

        matches = 0
        for r in range(len(s2)):
            right = s2[r]
            window[right] += 1

            if right in needs and window[right] == needs[right]:
                matches += 1
            elif right in needs and window[right] == needs[right] + 1:
                matches -= 1

            if r >= len(s1):
                left = s2[r - len(s1)]
                if left in needs and window[left] == needs[left]:
                    matches -= 1
                elif left in needs and window[left] == needs[left] + 1:
                    matches += 1
                window[left] -= 1

            if matches == len(needs.keys()):
                return True

        return False
