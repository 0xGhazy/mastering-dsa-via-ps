class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        result = 0
        for i in range(0, len(nums)):
            i_bin = str(bin(i)).replace("0b", "")
            if i_bin.count("1") == k:
                result += nums[i]
        return result
