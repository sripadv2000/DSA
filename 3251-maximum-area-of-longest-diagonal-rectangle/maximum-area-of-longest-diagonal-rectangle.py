class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        max_area = 0
        max_diagonal = 0
        
        for i in range(len(dimensions)):
            diagonal = (dimensions[i][0]**2 + dimensions[i][1]**2)**(0.5)
            
            if diagonal > max_diagonal or (diagonal == max_diagonal and dimensions[i][0] * dimensions[i][1] > max_area):
                max_diagonal = diagonal
                max_area = dimensions[i][0] * dimensions[i][1]
        
        return max_area