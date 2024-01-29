class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        words_list = s.split(" ")
        return " ".join(words_list[0:k])


x = Solution()

s = "Hello how are you Contestant"; k = 4
if (x.truncateSentence(s, k) == "Hello how are you"):
    print("Passed 1")

s = "What is the solution to this problem"; k = 4
if (x.truncateSentence(s, k) == "What is the solution"):
    print("Passed 2")

s = "chopper is not a tanuki"; k = 5
if (x.truncateSentence(s, k) == "chopper is not a tanuki"):
    print("Passed 3")
