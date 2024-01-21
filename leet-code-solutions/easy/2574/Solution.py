class Solution:
    def leftRightDifference(self, nums: list[int]) -> list[int]:
        left, right = [], []
        lsum, lsum = 0, 0

        if len(nums) == 1: return [0]

        for i in range(len(nums)):
            if i == 0: left.append(0)
            else:
                lsum = nums[i-1] + lsum
                left.append(lsum)

        for i in range(len(nums)):
            if i == len(nums) - 1: right.append(0)
            else:
                rsum = sum(nums[i+1:])
                right.append(rsum)
    
        return [ abs(left[i] - right[i]) for i in range(0, len(nums))]

# Old code
# class Solution:
#     def leftRightDifference(self, nums: List[int]) -> List[int]:
#         answer, left, right = [], [], []
#         if len(nums) == 1:
#             return [0]
#         # Get left & right sum array
#         reversed = nums[::-1][:-1]
#         for i in range(0, len(nums)):
#             left.append(sum(nums[0: i]))
#             right.append(sum(reversed[0: i]))
        
#         for i in range(0, len(left)):
#             answer.append(abs(left[i] - right[::-1][i]))
#         return answer


x = Solution()
nums = [10,4,8,3]

if(x.leftRightDifference(nums) == [15,1,11,22]):
    print("Passed")

nums = [1]
if(x.leftRightDifference(nums) == [0]):
    print("Passed")



