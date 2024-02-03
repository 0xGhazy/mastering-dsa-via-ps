from typing import List

class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        return (sum(salary) - (salary[0] + salary[-1])) / (len(salary) -2)
        

x = Solution()
print(x.average([4000,3000,1000,2000]))