# Link: https://leetcode.com/problems/find-the-difference/

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        l1 = [i for i in s]
        l2 = [i for i in t]
        for i in l1:
            l2.remove(i)
        return l2[0]
