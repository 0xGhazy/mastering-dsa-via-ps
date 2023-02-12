# Link: https://leetcode.com/problems/single-number/
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        unique_items = set(nums)
        for element in unique_items:
            if nums.count(element) > 1:
                pass
            else:
                return element
