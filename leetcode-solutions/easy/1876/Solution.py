class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        good_count, window_size = 0, 3
        if len(s) < window_size:
            return good_count
        for i in range(len(s) - window_size + 1):
            temp = s[i:i+window_size]
            if temp[0] != temp[1] and temp[1] != temp[2] and temp[0] != temp[2]:
                good_count += 1
        return good_count

x = Solution()
print(x.countGoodSubstrings("aababcabc"))
