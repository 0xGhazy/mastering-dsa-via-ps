# URL: https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/
class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        self.max_words = 0

        for statement in sentences:
            length = len(statement.split(" "))
            if self.max_words < length:
                self.max_words = length
        return self.max_words