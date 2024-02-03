class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        result = ""
        stack = []
        for c in s:
            if c == "(":
                stack.append(c)
            else:
                if len(stack) > 1:
                    result += stack.pop() + c
                    print("POPED OUT ()")
                else:
                    stack.pop()
            print(stack)
        return result


x = Solution()
# print(x.removeOuterParentheses("(()())(())") == "()()()")
print(x.removeOuterParentheses("(()())(())(()(()))") == "()()()()(())")
# print(x.removeOuterParentheses("()()") == "")

