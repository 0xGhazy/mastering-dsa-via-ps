class Solution:

    def searchRange(self, nums: list[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] > target:
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                low = high = mid
                while (low != 0):
                    if nums[low - 1] == target: low -= 1
                    else:break
                while (high != len(nums) - 1):
                    if nums[high + 1] == target: high += 1
                    else: break
                return [low, high]
        return [-1, -1]



# solution = Solution()

# nums1 = [5,7,7,8,8,10]
# target1 = 8
# if(solution.searchRange(nums1, target1) == [3, 4]):
#     print("Pass 1")


# nums2 = [5,7,7,8,8,10]
# target2 = 6
# if(solution.searchRange(nums2, target2) == [-1, -1]):
#     print("Pass 2")


# nums3 = []
# target3 = 0
# if(solution.searchRange(nums3, target3) == [-1, -1]):
#     print("Pass 3")
