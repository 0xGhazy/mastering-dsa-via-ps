class Solution:
    def reverseWords(self, s: str) -> str:
        init_words = [x for x in s.strip().split(" ")]
        return " ".join([x for x in init_words[::-1] if x != ""])
        

# solution = Solution()
# s = "the sky is blue"
# if(solution.reverseWords(s) == "blue is sky the"):
#     print("Pass 1")

# s = "  hello world  "
# if(solution.reverseWords(s) == "world hello"):
#     print("Pass 2")

# s = "a good   example"
# if(solution.reverseWords(s) == "example good a"):
#     print("Pass 3")