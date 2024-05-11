class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        i = 0
        while i < len(s):
            current = self.get_int_value(s[i])
            if i+1 < len(s):
                next = self.get_int_value(s[i+1])
                if current >= next:
                    result += current
                    i+=1
                else:
                    result += next - current
                    i+=2
            else:
                result += current
                i+=1
        return result

    
    def get_int_value(self, num: str) -> int:
        if num == "I":
            return 1
        elif num == "V":
            return 5
        elif num == "X":
            return 10
        elif num == "L":
            return 50
        elif num == "C":
            return 100
        elif num == "D":
            return 500
        elif num == "M":
            return 1000



x = Solution()
print(x.romanToInt("III") == 3)
print(x.romanToInt("LVIII") == 58)
print(x.romanToInt("MCMXCIV") == 1994)
