class Solution:
    def countPoints(self, rings: str) -> int:
        result_arr = [""] * 10
        result = 0
        i = 0
        while i < len(rings):
            current_pair = rings[i: i+2]
            result_arr[int(current_pair[1])] += current_pair[0]
            i += 2
        
        for i in result_arr:
            if "G" in i and "B" in i and "R" in i:
                result+=1
        return result

x = Solution()
print(x.countPoints("B0B6G0R6R0R6G9") == 1)
print(x.countPoints("B0R0G0R9R0B0G0") == 1)
print(x.countPoints("G4") == 0)