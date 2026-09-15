class NumMatrix:

    def __init__(self, matrix):
        self.matrix = matrix
        

    def sumRegion(self, row1, col1, row2, col2):
        count =0
        for i in range (row1,row2+1):
            for j in range(col1,col2+1):
                count+= self.matrix[i][j]
        
        return count

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)