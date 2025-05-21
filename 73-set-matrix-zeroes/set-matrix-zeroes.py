class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        rows_store = [1]*rows
        cols_store = [1]*cols

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    rows_store[i] = 0
                    cols_store[j] = 0
                    
        for i in range(rows):
            for j in range(cols):
                if rows_store[i] == 0 or cols_store[j] == 0:
                    matrix[i][j] = 0
        return matrix