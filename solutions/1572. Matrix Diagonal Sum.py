class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        s = 0
        d1 = [mat[i][i] for i in range(len(mat))]
        d2 = [mat[i][len(mat)-i-1] for i in range(len(mat))]
        for i in range(0, len(d1)):
            s += d1[i] + d2[i]
        if len(d1) % 2 != 0:
            mid = (len(d1) // 2)
            s -= d1[mid]
        return s