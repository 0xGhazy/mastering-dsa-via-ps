class Solution:
    def maxWidthOfVerticalArea(self, points: list[list[int]]) -> int:
        max_wids = -1000
        sorted_list = sorted(points, key=lambda x: x[0])
        i = 0
        while i+1 < len(sorted_list):
            current_max = sorted_list[i+1][0] - sorted_list[i][0]
            if(current_max > max_wids):
                max_wids = current_max
            i += 1
        return max_wids



c = [[8,7],[9,9],[7,4],[9,7]]
x = Solution()
print(x.maxWidthOfVerticalArea(c))

        