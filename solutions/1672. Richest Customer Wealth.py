# URL: https://leetcode.com/problems/richest-customer-wealth
class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        # calculate the sum of inner arrays
        self.max_wealth = 0
        for account in accounts:
            result = 0
            for i in account:
                result += i
            if result > self.max_wealth:
                self.max_wealth = result
        return self.max_wealth
