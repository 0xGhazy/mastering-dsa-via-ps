class Solution:

    def rev_word(self, word: str):
        return word[::-1]

    def reverseWords(self, s: str) -> str:
        word_list = s.split(" ")
        start_index = 0
        last_index = len(word_list) - 1
        result = ""
        for word in word_list:
            if(start_index < last_index):
                result += f"{self.rev_word(word)} "
            else:
                result += f"{self.rev_word(word)}"
            start_index += 1
        return result
    

    # I found this solution on Leetcode (Easy - simple)
    # https://leetcode.com/problems/reverse-words-in-a-string-iii/solutions/3036362/python3-reverse-words-in-a-string-simple/?languageTags=python
    # class Solution(object):
    #     def reverseWords(self, s):
    #         """
    #         :type s: str
    #         :rtype: str
    #         """
    #         s = map(lambda x: x[::-1], s.split(' '))
    #         return ' '.join(s)

s = "Let's take LeetCode contest"
x = Solution()
print(x.reverseWords(s))