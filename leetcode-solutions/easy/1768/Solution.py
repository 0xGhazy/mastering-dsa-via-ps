

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ""
        mx_index = max(len(word1), len(word2))
        for i in range(0, mx_index):
            if (i <= len(word1) -1):
                result += word1[i]
            if(i <= len(word2) -1):
                result += word2[i]
        return result


x = Solution().mergeAlternately("abcd", "pq")