class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        zero_already = False
        for row in range(len(matrix)):
            if matrix[row][0] == 0:
                zero_already = True
            for col in range(1, len(matrix[row])):
                if matrix[row][col] == 0:
                    matrix[row][0] = 0
                    matrix[0][col] = 0

        for row in range(len(matrix) - 1, -1, -1):
            for col in range(len(matrix[row]) - 1, 0, -1):
                if matrix[row][0] == 0 or matrix[0][col] == 0:
                    matrix[row][col] = 0
            if zero_already:
                matrix[row][0] = 0
