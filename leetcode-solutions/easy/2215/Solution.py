class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        result = []
        result.append(set(nums1).difference(set(nums2)))
        result.append(set(nums2).difference(set(nums1)))
        return result # 132 ms

        ## 524 ms
        # n1, n2 = {}, {}
        # for i in nums1:
        #     if i not in nums2:
        #         n1[i] = True
        # for i in nums2:
        #     if i not in nums1:
        #         n2[i] = True
        # return [list(n1.keys()), list(n2.keys())]

# x = Solution()
# nums1 = [1,2,3]; nums2 = [2,4,6]
# if x.findDifference(nums1, nums2) == [[1,3],[4,6]]:
#     print("Passed")


# nums1 = [1,2,3,3]; nums2 = [1,1,2,2]
# if x.findDifference(nums1, nums2) == [[3],[]]:
#     print("Passed")










