# Link: https://leetcode.com/problems/find-target-indices-after-sorting-array/
class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        index_list = []
        for i, num in enumerate(sorted(nums)):
            if num == target:
                index_list.append(i)
        return index_list
