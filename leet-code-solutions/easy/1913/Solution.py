class Solution:
    def maxProductDifference(self, nums: list[int]) -> int:
        # get the max two numbers to get the maximum product value
        px1 = max(nums)
        nums.remove(px1)
        py1 = max(nums)
        left = (px1 * py1)
        # get the mmin two product
        px2 = min(nums)
        nums.remove(px2)
        py2 = min(nums)
        right = (px2 * py2)
        return (left - right)

