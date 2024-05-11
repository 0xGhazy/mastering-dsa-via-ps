class Solution:
    def maximumStrongPairXor(self, nums: list[int]) -> int:
        max_strong_pairs = -1
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                n1, n2 = nums[i], nums[j]
                if abs(n1 - n2) <= min(n1, n2):
                    strong_xor = n2^n1
                    max_strong_pairs = max(strong_xor, max_strong_pairs)
        return max_strong_pairs


x = Solution()
nums = [1,2,3,4,5]
if x.maximumStrongPairXor(nums) == 7:
    print("Passed 1")

nums = [10,100]
if x.maximumStrongPairXor(nums) == 0:
    print("Passed 2")

nums = [5,6,25,30]
if x.maximumStrongPairXor(nums) == 7:
    print("Passed 3")

nums = [1,1,10,3,9]
if x.maximumStrongPairXor(nums) == 3:
    print("Passed 4")