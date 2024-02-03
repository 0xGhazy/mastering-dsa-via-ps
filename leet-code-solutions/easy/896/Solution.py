from typing import List

class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        is_increasing = True if nums[0] <= nums[-1] else False
        if is_increasing:
            for i in range(len(nums)-1):
                if nums[i] > nums[i+1]:
                    return False
        else:
            for i in range(len(nums)-1):
                if nums[i] < nums[i+1]:
                        return False
        return True


x = Solution()
print(x.isMonotonic([1,2,2,3]) == True)
print(x.isMonotonic([6,5,4,4]) == True)
print(x.isMonotonic([1,3,2]) == False)