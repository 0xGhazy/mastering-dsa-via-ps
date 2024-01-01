class Solution:
    def findIntersectionValues(self, nums1: list[int], nums2: list[int]) -> list[int]:
        result = [0, 0]
        nums1_map, nums2_map = {}, {}

        for value in nums1:
            if nums1_map.get(value) == None: nums1_map[value] = 1
            else: nums1_map[value] = nums1_map.get(value) + 1

        for value in nums2:
            if nums2_map.get(value) == None: nums2_map[value] = 1
            else: nums2_map[value] = nums2_map.get(value) + 1


        for i in nums2_map.keys():
            if nums1_map.get(i): result[0] += nums1_map.get(i)
        
        for i in nums1_map.keys():
            if nums2_map.get(i): result[1] += nums2_map.get(i)

        return result


# solution = Solution()

# nums1 = [4,3,2,3,1]
# nums2 = [2,2,5,2,3,6]
# if solution.findIntersectionValues(nums1, nums2) == [3, 4]:
#     print("Pass 1")


# nums1 = [3,4,2,3]
# nums2 = [1,5]
# if solution.findIntersectionValues(nums1, nums2) == [0, 0]:
#     print("Pass 2")