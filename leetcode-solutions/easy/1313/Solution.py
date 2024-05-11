class Solution:
    def decompressRLElist(self, nums: list[int]) -> list[int]:
        result = []
        init_freq_index, init_val_index = 0, 1
        while init_val_index < len(nums):
            freq = nums[init_freq_index]
            value = nums[init_val_index]
            for i in self.generate_numbers(freq, value):
                result.append(i)
            init_freq_index += 2
            init_val_index += 2
        return result
    
    def generate_numbers(self, freq: int, value: int):
        return [value] * freq 


x = Solution()

nums = [1,2,3,4]; output = [2,4,4,4]
if(x.decompressRLElist(nums) == output):
    print("Passed")

nums = [1,1,2,3]; output = [1,3,3]
if(x.decompressRLElist(nums) == output):
    print("Passed")
