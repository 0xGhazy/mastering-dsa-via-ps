from typing import List
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        # calculate the sum of inner arrays
        max_wealth = 0
        for account in accounts:
            account_sum = sum(account)
            max_wealth = max(max_wealth, account_sum)
        return max_wealth
