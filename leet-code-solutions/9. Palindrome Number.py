class Solution:
    def isPalindrome(self, x: int) -> bool:
        reversed_int = 0
        number = x
        if number >= 0:
            while number != 0:
                last_digit = number % 10
                reversed_int = (reversed_int * 10) + last_digit
                number = number // 10
            if reversed_int == x:
                return True
            else:
                return False
        else:
            return False
