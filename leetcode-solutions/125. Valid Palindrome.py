class Solution:
    def remove_non_alphanumeric(self, s: str) -> str:
        result = ""
        s = s.lower()
        for i in s:
            if i.isalnum():
                result += i
        return result

    def isPalindrome(self, s: str) -> bool:
        if(len(s) == 1):
            return True
        else:
            s = self.remove_non_alphanumeric(s)
            f = 0
            l = len(s) -1
            while (f < l):
                if(s[f] != s[l]):
                    return False
                f += 1
                l -= 1
        return True


t1 = "A man, a plan, a canal: Panama"
t2 = "race a car"
t3 = " "
x = Solution()
print(x.isPalindrome(t3))