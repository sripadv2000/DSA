class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        area, diagonal = 0, 0
        for i in range(len(dimensions)):
            length = dimensions[i][0]
            breadth = dimensions[i][1]
            temp_diagonal = length**2 + breadth**2
            if (temp_diagonal > diagonal) or (temp_diagonal == diagonal and length * breadth > area) :
                diagonal = temp_diagonal
                area = length * breadth
        return area