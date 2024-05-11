
class Solution:
    def reverseVowels(self, s: str) -> str:
        v = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        s = [x for x in s]
        f_index = 0
        l_index = len(s) - 1
        while(f_index < l_index):
            if(s[f_index] in v and s[l_index] in v):
                s[f_index], s[l_index] = s[l_index], s[f_index]
                f_index += 1
                l_index -= 1
            elif s[f_index] in v and s[l_index] not in v:
                l_index -= 1
            elif s[f_index] not in v and s[l_index] in v:
                f_index += 1
            else:
                f_index += 1
                l_index -= 1
        return "".join(s)
    

x = Solution()
x = x.reverseVowels("leetcode")
print(x)