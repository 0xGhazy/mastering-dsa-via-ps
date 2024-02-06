from typing import List

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        nums_dict = {}
        for i in nums:
            if i not in nums_dict.keys():
                nums_dict[i] = i
            else:
                nums_dict[i] = 0
        return sum(nums_dict.values())


x = Solution()
print(x.sumOfUnique([1,2,3,2]) == 4)
print(x.sumOfUnique([1,1,1,1,1]) == 0)
print(x.sumOfUnique([1,2,3,4,5]) == 15)