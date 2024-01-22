class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        for i in range(len(nums)):
            temp = 0
            if nums[i] < 0 and nums[i+1] < 0:
                for j in range(i, len(nums)):
                    if (nums[j] > 0):
                        temp = nums[i + 1]
                        nums[i + 1] = nums[j]
                        nums[j] = temp
            
            elif nums[i] > 0 and nums[i+1] > 0:
                for j in range(i, len(nums)):
                    if (nums[j] < 0):
                        temp = nums[i + 1]
                        nums[i + 1] = nums[j]
                        nums[j] = temp
            print(nums)
                




x = Solution()
nums = [3,1,-2,-5,2,-4]
if x.rearrangeArray(nums) == [3,-2,1,-5,2,-4]:
    print("Passing 1")

nums = [-1, 1]
if x.rearrangeArray(nums) == [1, -1]:
   print("Passing 2")
        




