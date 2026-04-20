class Solution:
    def fill(self, matrix, i, j):
        a = len(matrix)
        b = len(matrix[0])
        for x in range(b):
            matrix[i][x] = 0
        for y in range(a):
            matrix[y][j] = 0

    def setZeroes(self, matrix: List[List[int]]) -> None:
        zeros = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    zeros.append((i, j))
        for i, j in zeros:
            self.fill(matrix, i, j)