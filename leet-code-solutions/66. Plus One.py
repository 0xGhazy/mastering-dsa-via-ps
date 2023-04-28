# Link: https://leetcode.com/problems/plus-one/
class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        my_number = int("".join(str(i) for i in digits)) + 1
        return [int(i) for i in str(my_number)]
