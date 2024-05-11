from typing import List
class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        visited = set(nums) # allowing us to lookup in O(n) time
        result = 0
        for num in nums:
            if num + diff in visited and num + diff*2 in visited:
                result += 1
        return result

x = Solution()
print(x.arithmeticTriplets(nums = [0,1,4,6,7,10], diff = 3) == 2)
print(x.arithmeticTriplets(nums = [4,5,6,7,8,9], diff = 2) == 2)