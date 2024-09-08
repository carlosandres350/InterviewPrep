class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        #tranpose the matrix
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            
        print(matrix)
        print(n //2 )
        #reflect the matrix
        for i in range(n):
            for j in range(n // 2):
                # i = 0
                # j = 0
                # 1 4 7
                # 2 5 8
                # 3 6 9
                matrix[i][j], matrix[i][n - j - 1] = matrix[i][n-j-1], matrix[i][j], 
                # matrix[0][0] = matrix[0][2]
                # matrix[0][2] = matrix[0][0]
        return matrix