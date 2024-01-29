from typing import List

class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        final_sum = 0
        final_sum += sum(arr[0::])
        if len(arr) % 2 != 0 and len(arr) != 1:
            final_sum += final_sum
        for i in range (3, len(arr)):
            if i % 2 != 0:
                for j in range (len(arr) - i + 1):
                # do sliding window here 
                    window = arr[j:j+i]
                    final_sum += sum(window)
        return final_sum

x = Solution()
print(x.sumOddLengthSubarrays([1,4,2,5,3]) == 58)
print(x.sumOddLengthSubarrays([1,2]) == 3)
print(x.sumOddLengthSubarrays([10,11,12]) == 66)
