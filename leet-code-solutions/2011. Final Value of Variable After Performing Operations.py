# URL: https://leetcode.com/problems/final-value-of-variable-after-performing-operations/
class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        self.x = 0
        for i in operations:
            if i == "++X" or i == "X++":
                self.x += 1
            else:
                self.x -= 1
        return self.x
