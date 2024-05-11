# URL: https://leetcode.com/problems/reverse-integer/
class Solution:
    
    def validate_reverse(self, result: int) -> int:
        if result <= -2147483648 or result >= 2147483647:
            return 0
        else:
            return result

    def reverse(self, x: int) -> int:
        # check for the sign
        result = 0
        if x > 0:
            while x != 0:
                last_digit = x % 10
                result = (result * 10) + last_digit
                x = x // 10
            return self.validate_reverse(result)
        else:
            x *= -1
            while x != 0:
                last_digit = x % 10
                result = (result * 10) + last_digit
                x = x // 10
            return self.validate_reverse(result * -1)



if __name__ == '__main__':
    x = Solution()
    print(x.reverse(1563847412))