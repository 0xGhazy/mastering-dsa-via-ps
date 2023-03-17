class Solution:
    def maximumCount(self, nums: list[int]) -> int:
        pos_list = len([x for x in nums if x > 0])
        neg_list = len([x for x in nums if x < 0])
        return max(pos_list, neg_list)