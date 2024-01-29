class Solution:
    def differenceOfSum(self, nums: list[int]) -> int:
        list_sum = sum(nums[0::])
        digits_sum = 0
        for num in nums:
            digits_sum += self.get_digits(num)
        return abs(digits_sum - list_sum)

    def get_digits(self, number: int):
        digits_sum = 0
        while number > 0:
            digits_sum += number % 10
            number //= 10
        return digits_sum


x = Solution()
if x.differenceOfSum([1,15,6,3]) == 9:
    print("Passed 1")

if x.differenceOfSum([1,2,3,4]) == 0:
    print("Passed 2")
