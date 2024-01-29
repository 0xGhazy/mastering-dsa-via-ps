class Solution:
    def finalString(self, s: str) -> str:
        text = ""
        for i in s:
            if i != "i":
                text += i
            else:
                text = text[::-1]
        return text




x = Solution()
print(x.finalString("string")  == "rtsng")
print(x.finalString("poiinter")  == "ponter")