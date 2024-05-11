from typing import List

class Solution:

    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = [x**2 for x in nums]
        return sorted(result)

x = Solution()
print(x.sortedSquares([-7,-3,2,3,11]))