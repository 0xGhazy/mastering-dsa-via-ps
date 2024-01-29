class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        max_pair_count = 0
        for i in range(0, len(words)):
            pass
            for j in range (i+1, len(words)):
                if words[i] == words[j][::-1]:
                    max_pair_count+=1
        return max_pair_count
        