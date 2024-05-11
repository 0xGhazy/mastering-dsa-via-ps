class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # [2::] to reomove '0b' binary flag.
        int_a, int_b = int(a, 2), int(b, 2)
        return bin(int_a+int_b)[2::]

        