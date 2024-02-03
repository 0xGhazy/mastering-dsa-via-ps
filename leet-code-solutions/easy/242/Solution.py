class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        arr = [0] * 26
        for i in s:
            arr[ord(i) - ord('a')] += 1
        for i in t:
            arr[ord(i) - ord('a')] -= 1
        for i in range(len(arr)):
            if arr[i] != 0:
                return False
        return True
        
x = Solution()
print(x.isAnagram(s="rat", t="car"))