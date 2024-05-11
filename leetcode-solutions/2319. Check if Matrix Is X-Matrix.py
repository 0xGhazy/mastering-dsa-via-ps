class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        i = 0
        j = len(grid) - 1
        for row in grid:
            # print(i, j)
            first = row[i]
            second =  row[j]
            if first != 0 and second != 0:
                if i != j:
                    row.remove(first)
                    row.remove(second)
                else:
                    row.remove(first)
                i += 1
                j -= 1
            else:
                return False
        
        for row in range(0, len(grid)):
            for column in range(0, len(grid[row])):
                if grid[row][column] != 0:
                    return False
        return True