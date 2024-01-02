class Solution:
    def countPairs(self, nums: list[int], target: int) -> int:
        result = 0
        for i in range(0, len(nums)):
            for j in range(len(nums) - 1, -1, -1):
                if (i < j) and (nums[i] + nums[j] < target):
                    result += 1
        return result



solution = Solution()

nums = [-1,1,2,3,1]
target = 2
if solution.countPairs(nums, target) == 3:
    print("Pass 1")

nums = [-6,2,5,-2,-7,-1,3]
target = -2
if solution.countPairs(nums, target) == 10:
    print("Pass 2")

