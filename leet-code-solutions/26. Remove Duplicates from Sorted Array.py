# Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        self.ex_length =  0
        for i in range(len(nums)):
            if i < len(nums) - 1 and nums[i] == nums[i + 1]:
                continue
            else:
                nums[self.ex_length] = nums[i]
                self.ex_length += 1
        return self.ex_length
