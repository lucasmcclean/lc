class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        found = [False, False, False]

        a, b, c = target

        for x, y, z in triplets:
            if x  > a or y > b or z > c:
                continue

            if x == a:
                found[0] = True
            if y == b:
                found[1] = True
            if z == c:
                found[2] = True

            if all(found):
                break

        return all(found)
