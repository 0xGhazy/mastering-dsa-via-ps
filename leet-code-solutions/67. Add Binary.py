# Link: https://leetcode.com/problems/add-binary/
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # [2::] to reomove '0b' binary flag.
        return str(bin(int(a, 2) + int(b, 2)))[2::]
        