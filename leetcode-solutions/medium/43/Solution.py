class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n1, n2 = 0, 0
        for i in range(len(num1)):
            n1 += 10**i * (ord(num1[::-1][i]) - ord("0"))
        for i in range(len(num2)):
            n2 += 10**i * (ord(num2[::-1][i]) - ord("0"))
        return str(n1 * n2)


x = Solution()
print(x.multiply("2", "3") == "6")
print(x.multiply("123", "456") == "56088")