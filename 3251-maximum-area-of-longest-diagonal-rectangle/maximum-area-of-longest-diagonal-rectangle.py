class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        area, diagonal = 0, 0
        for i in range(len(dimensions)):
            temp_diagonal = (dimensions[i][0])**2 + (dimensions[i][1])**2
            if (temp_diagonal > diagonal) or (temp_diagonal == diagonal and dimensions[i][0] * dimensions[i][1] > area) :
                diagonal = temp_diagonal
                area = dimensions[i][0] * dimensions[i][1]
        return area