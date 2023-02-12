# Link: https://leetcode.com/problems/move-zeroes

class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # count all zeros 
        zeroes_count = nums.count(0)
        for _ in range(0, zeroes_count):
            nums.remove(0)
            nums.append(0)
