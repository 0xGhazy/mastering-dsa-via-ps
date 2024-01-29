class Solution:
    def x(self, nums, k):
        nums = sorted(nums)
        max_score = 0
        for i in range(0, k):
            num = nums[-1]
            nums.pop()
            nums.append(num+1)
            max_score += num
        return max_score



x = Solution()
nums = [1, 2, 3, 4, 5]; k = 3
print(x.x(nums, k))
nums = [5, 5, 5]; k = 2
print(x.x(nums, k))
