from typing import List
class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        # create a list of unique sets

        result = 0
        for i in range(len(nums)):
            set_to_check = set()
            for j in range(i, len(nums)):
                set_to_check.add(nums[j])
                result += len(set_to_check)**2
        return result        


x = Solution()
print(x.sumCounts([1,2,1]) == 15)
print(x.sumCounts([1,1]) == 3)