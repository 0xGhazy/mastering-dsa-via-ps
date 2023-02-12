# Link: https://leetcode.com/problems/remove-element/submissions/

class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        while nums.count(val):
            nums.remove(val)
        return len(nums)
