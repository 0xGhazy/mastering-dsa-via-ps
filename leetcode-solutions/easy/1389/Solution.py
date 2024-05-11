class Solution:
    def createTargetArray(self, 
                          nums: list[int], 
                          index: list[int]) -> list[int]:
        target = ["-"] * len(nums)
        for i in range(len(nums)):
            element, idx = nums[i], index[i]
            if target[idx] == "-":
                target[idx] = element
            else:
                target.insert(idx, element)
        return [ x for x in target if x != "-"]
    
x = Solution()


nums = [0,1,2,3,4]
index = [0,1,2,2,1]
output = [0,4,1,3,2]
result = x.createTargetArray(nums, index)
if(result == output):
    print("Passed")

nums = [1,2,3,4,0]
index = [0,1,2,3,0]
output = [0,1,2,3,4]
result = x.createTargetArray(nums, index)
if(result == output):
    print("Passed")