# Link: https://leetcode.com/problems/intersection-of-two-arrays/submissions/
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = set(nums1)
        nums2 = set(nums2)
        result = []
        for i in nums2:
            if i in nums1 and i not in result:
                result.append(i)
        return result
        