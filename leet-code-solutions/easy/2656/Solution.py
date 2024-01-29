from typing import List
class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        max_score = 0
        for i in range(0, k):
            num = nums[-1]
            nums.pop()
            nums.append(num+1)
            max_score += num
        return max_score