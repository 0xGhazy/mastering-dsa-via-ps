class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        low, high = 0, len(s) - 1
        new_s = [c for c in s]
        while low < high:
            if s[low] != s[high]:
                if(s[low] < s[high]):
                    new_s[high] = s[low]
                else:
                    new_s[low] = s[high]
            high -= 1
            low += 1
        return "".join(new_s)

    
sovle = Solution().makeSmallestPalindrome

if(sovle("egcfe") == "efcfe"):
    print("Pass 1")

if(sovle("abcd") == "abba"):
    print("Pass 2")

if(sovle("seven") == "neven"):
    print("Pass 3")

if(sovle("bhh") == "bhb"):
    print("Pass 4")

