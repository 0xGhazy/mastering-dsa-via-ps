from typing import List
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        left_diagonal, right_diagonal = 0, 0
        for i in range(0, len(mat)):
            left_diagonal += mat[i][i]
            right_diagonal += mat[i][len(mat)-i-1]

        is_even = len(mat) % 2
        if is_even != 0:
            # remove the duplicate center point from the diagonals
            right_diagonal -= mat[len(mat) // 2][len(mat) // 2]
        return right_diagonal + left_diagonal