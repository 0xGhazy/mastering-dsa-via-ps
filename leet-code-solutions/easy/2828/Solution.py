class Solution:
    def isAcronym(self, words: list[str], s: str) -> bool:
        s_list = [c for c in s]
        if len(s_list) != len(words):
            return False
        i = 0
        for word in words:
            if word[0] != s_list[i]:
                return False
            i += 1
        return True


x = Solution()
words = ["alice","bob","charlie"]; s = "abc"
if x.isAcronym(words, s) == True:
    print("Passed")

words = ["an","apple"]; s = "a"
if x.isAcronym(words, s) == False:
    print("Passed")

words = ["never","gonna","give","up","on","you"]; s = "ngguoy"
if x.isAcronym(words, s) == True:
    print("Passed")