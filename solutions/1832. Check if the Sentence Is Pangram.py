class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        char_table = {}
        for eng_char in sentence:
            if eng_char in char_table.keys():
                char_table[eng_char] += 1
            else:
                char_table[eng_char] = 1
        return len(char_table.keys()) >= 26


sentence = "thequickbrownfoxjumpsoverthelazydog"
x = Solution()
print(x.checkIfPangram(sentence))
