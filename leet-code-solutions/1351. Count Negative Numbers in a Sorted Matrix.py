class Solution:
    def countNegatives(self, grid: list[list[int]]) -> int:
        negatives_count = 0
        for arr in grid:
            negatives_count += len([x for x in arr if x < 0])
        return negatives_count
    
