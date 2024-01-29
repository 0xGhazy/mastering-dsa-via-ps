class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        count = 0
        num_as_string = str(num)
        for i in range(len(num_as_string)-k+1):
            number = int(num_as_string[i: i+k])
            if number == 00: continue
            elif num % number == 0:
                count += 1
        return count

x = Solution()
nums, k = 240, 2 
if x.divisorSubstrings(nums, k) == 2:
    print("Passed 1")

nums, k = 430043, 2
if x.divisorSubstrings(nums, k) == 2:
    print("Passed 2")
