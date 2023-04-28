#URL: https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/
class Solution:
    # Brute force for each array element.
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        result = []
        for i in nums:
            nums_of_smaller = 0
            for j in nums:
                if j < i:
                    nums_of_smaller += 1
            result.append(nums_of_smaller)
        return result
