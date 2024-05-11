from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows_count = len(matrix)
        colums_count = len(matrix[0])
        rows_with_zeros = [False] * rows_count 
        colums_with_zeros = [False] * colums_count

        # check for zero's in matrix
        for i in range(rows_count):
            for j in range(colums_count):
                if matrix[i][j] == 0:
                    rows_with_zeros[i], colums_with_zeros[j] = True, True

        # change row to zero
        for i in range(rows_count):
            if rows_with_zeros[i]:
                for j in range(colums_count):
                    matrix[i][j] = 0
        
        # change col to zero
        for i in range(colums_count):
            if colums_with_zeros[i]:
                for j in range(rows_count):
                    matrix[j][i] = 0

        # uncomment the next line to test the result
        # return matrix


x = Solution()
print(x.setZeroes([[1,1,1],[1,0,1],[1,1,1]]) == [[1,0,1],[0,0,0],[1,0,1]])
print(x.setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]]) == [[0,0,0,0],[0,4,5,0],[0,3,1,0]])
print(x.setZeroes([[0,0,0,5],[4,3,1,4],[0,1,1,4],[1,2,1,3],[0,0,1,1]]) == \
      [[0,0,0,0],[0,0,0,4],[0,0,0,0],[0,0,0,3],[0,0,0,0]])