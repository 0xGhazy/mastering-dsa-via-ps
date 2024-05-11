
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        first_word = sorted(strs)[0]
        index = 0
        for i in range(0, len(first_word)):
            for word in strs:
                if word[index] != first_word[index]:
                    return result
            result += first_word[index]
            index += 1
        return result
