class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        for i in range(0, len(nums)):
            j = i + 1
            if j < len(nums):
                if nums[i] == nums[j] and abs(i - j) <= k:
                    return True
        return False


"""

Given an integer array nums and an integer k,
return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.
"""



t = [1,2,3,1]
k = 3

solution = Solution()
result = solution.containsNearbyDuplicate(t, k)
print(result)
