from typing import List

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        base_gradient = self.calc_gradient(coordinates[0], coordinates[1])
        for i in range(len(coordinates)-1):
            if self.calc_gradient(coordinates[i], coordinates[i+1]) != base_gradient:
                return False
        return True

    
    def calc_gradient(self, p1: List[int], p2: List[int]) -> int:
        y_diff = (p2[1] - p1[1])
        x_diff = (p2[0] - p1[0])
        if x_diff == 0:
            return False
        else:
            return y_diff/x_diff


x = Solution()
print(x.checkStraightLine([[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]) == True) 
print(x.checkStraightLine([[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]) == False)
print(x.checkStraightLine([[0,0],[0,1],[0,-1]]))