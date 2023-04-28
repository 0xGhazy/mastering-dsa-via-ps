# Link: https://leetcode.com/problems/search-insert-position/

class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            guess = nums[mid]
            if guess < target:
                low = mid + 1
            if guess > target:
                high = mid - 1
            if guess == target:
                return mid
        return low
            
x = Solution()
print(x.searchInsert([1,3,5,6], 2))
