# Link: https://leetcode.com/problems/contains-duplicate/
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        # if len nums != set it'll be have duplicates
        return len(nums) != len(set(nums))
        