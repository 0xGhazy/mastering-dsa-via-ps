class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().split(" ")[-1].strip())


x = Solution()
print(x.lengthOfLastWord(s = "Hello World") == 5)
print(x.lengthOfLastWord(s = "   fly me   to   the     moon  ") == 4)
print(x.lengthOfLastWord(s = "luffy is still joyboy") == 6)