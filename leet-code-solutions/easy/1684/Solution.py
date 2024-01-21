class Solution:
    def countConsistentStrings(self, allowed: str, words: list[str]) -> int:
        allowed_list = [c for c in allowed]
        consistent_count = 0
        for word in words:
            if(self.isConsistent(allowed_list, word)): consistent_count+=1
        return consistent_count

    def isConsistent(self, allowed_list: str, word: str) -> bool:
        for c in word:
            if c not in allowed_list:
                return False
        return True


x = Solution()
allowed = "ab"; words = ["ad","bd","aaab","baa","badab"]
if x.countConsistentStrings(allowed, words) == 2:
    print("Passed")

allowed = "abc"; words = ["a","b","c","ab","ac","bc","abc"]
if x.countConsistentStrings(allowed, words) == 7:
    print("Passed")