class Solution:
    def canBeIncreasing(self, nums: list[int]) -> bool:
        for i in range(len(nums)):
            # Get all elements of the lest excluding the elements of the index i
            temp_list = nums[:i] + nums[i+1:] # simulating the remove operation
            # check if we didn't have duplicates and it's sorted -strictly increasing-
            if temp_list == sorted(set(temp_list)):
                return True
        return False


x = Solution()

nums = [1,2,10,5,7]
if (x.canBeIncreasing(nums) == True):
    print("Passed 1")

nums = [2,3,1,2]
if (x.canBeIncreasing(nums) == False):
    print("Passed 2")

nums = [1,1,1]
if (x.canBeIncreasing(nums) == False):
    print("Passed 3")


nums = [1,2,3]
if (x.canBeIncreasing(nums) == True):
    print("Passed 4")

nums = [1,1]
if (x.canBeIncreasing(nums) == True):
    print("Passed 5")