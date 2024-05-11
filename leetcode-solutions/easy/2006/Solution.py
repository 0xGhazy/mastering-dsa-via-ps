class Solution:
    def countKDifference(self, nums: list[int], k: int) -> int:
        k_diff = 0
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                if abs(nums[i] - nums[j]) == k:
                    k_diff += 1
        return k_diff


x = Solution()
print(x.countKDifference([1,2,2,1], 1) == 4)
print(x.countKDifference([1,3], 3) == 0)
print(x.countKDifference([3,2,1,5,4], 2) == 3)