from typing import List

class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        our_max = nums[-1]
        answer = -1
        # -2 to get the element before the last element
        i = len(nums) - 2
        while(i >= 0):
            if(nums[i] < our_max):
                # get the maximum difference
                answer = max(answer, our_max - nums[i])
            our_max = max(our_max, nums[i])
            i -= 1
        return answer


nums = [1,5,2,10]
x = Solution()
print(x.maximumDifference(nums))
