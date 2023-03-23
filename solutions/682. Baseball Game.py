from typing import List 


class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for op in operations:
            if op == "+":
                stack.append(int(stack[-1] + stack[-2]))
            elif op == "D":
                stack.append(int(stack[-1] *2))
            elif op == "C":
                stack.pop()
            else:
                stack.append(int(op))
        result = 0
        for i in stack:
            result += i
        return result



ops = ["1","C"]
x = Solution()
print(x.calPoints(ops))
