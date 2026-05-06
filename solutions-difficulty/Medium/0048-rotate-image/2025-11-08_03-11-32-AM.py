class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        '''
        n - row = new row
        n - col = new col
        '''
        n = len(matrix) - 1

        for i in range(len(matrix)//2):
            for j in range(i, n - i):
                print(i, j, matrix[i][j])
                matrix[i][j], matrix[j][n - i] = matrix[j][n - i], matrix[i][j]
                print(matrix)
                matrix[i][j], matrix[n - i][n - j] = matrix[n - i][n - j], matrix[i][j]
                print(matrix)
                matrix[i][j], matrix[n - j][i] = matrix[n - j][i], matrix[i][j]

