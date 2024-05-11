class Solution:
    def numberOfMatches(self, n: int) -> int:
        matches_count = 0
        while n > 1:
            if n % 2 == 0:
                matches_count += (n//2)
                n = (n//2)
            else:
                matches_count += (n-1)//2
                n = (n//2) + 1
        return matches_count


x = Solution()
print(x.numberOfMatches(7) == 6)
print(x.numberOfMatches(14) == 13)