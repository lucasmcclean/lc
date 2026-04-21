class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        last = len(matrix[0]) - 1

        mid = 0
        t, b = 0, len(matrix) - 1
        while t <= b:
            mid = t + (b - t) // 2
            if matrix[mid][last] >= target:
                if mid == 0 or matrix[mid - 1][last] < target:
                    break
                else:
                    b = mid - 1
            else:
                    t = mid + 1

        row = mid
        l, r = 0, len(matrix[row]) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if matrix[row][mid] < target:
                l = mid + 1
            elif matrix[row][mid] > target:
                r = mid - 1
            else:
                return True

        return False
