class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        f_index = 0
        l_index = word.find(ch)
        return word[f_index:l_index+1][::-1] + word[l_index+1::]

