# Link: https://leetcode.com/problems/add-to-array-form-of-integer/
class Solution:
    def addToArrayForm(self, num: list[int], k: int) -> list[int]:
        my_number = int("".join(str(i) for i in num)) + k
        return [int(i) for i in str(my_number)]