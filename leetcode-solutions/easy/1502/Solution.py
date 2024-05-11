from typing import List

class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        diff = arr[0] - arr[1]
        for i in range(len(arr) -1):
            if arr[i] - arr[i+1]!= diff:
                return False
        return True


x = Solution()
print(x.canMakeArithmeticProgression([3,5,1]) == True)
print(x.canMakeArithmeticProgression([1,2,4]) == False)