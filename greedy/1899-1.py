class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        secured = [False, False, False]

        for t in triplets:
            if not secured[0] and t[0] == target[0]:
                if t[1] <= target[1] and t[2] <= target[2]:
                    secured[0] = True

            if not secured[1] and t[1] == target[1]:
                if t[0] <= target[0] and t[2] <= target[2]:
                    secured[1] = True

            if not secured[2] and t[2] == target[2]:
                if t[0] <= target[0] and t[1] <= target[1]:
                    secured[2] = True

            if all(secured):
                return True

        return False
