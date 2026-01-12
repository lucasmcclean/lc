class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        LAST = len(matrix[0]) - 1

        row = 0
        t, b = 0, len(matrix) - 1
        while t <= b:
            mid = t + (b - t) // 2
            if matrix[mid][LAST] < target:
                t = mid + 1
            elif matrix[mid][LAST] > target:
                row = mid
                if mid == 0 or matrix[mid - 1][LAST] < target:
                    break
                b = mid - 1
            else:
                return True

        l, r = 0, LAST
        while l <= r:
            mid = l + (r - l) // 2
            if matrix[row][mid] < target:
                l = mid + 1
            elif matrix[row][mid] > target:
                r = mid - 1
            else:
                return True

        return False
