
class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        f_index = 0;
        l_index = len(s) - 1
        while(f_index < l_index):
            s[f_index], s[l_index] = s[l_index], s[f_index]
            f_index += 1
            l_index -= 1
        return s





test_case_1 = ["h","e","l","l","o"]
test_case_2 = ["H","a","n","n","a","h"]

x = Solution()
print(x.reverseString(test_case_1))