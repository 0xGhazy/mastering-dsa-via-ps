class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        target, count = "B" * k, 1000
        if blocks.count(target) > 0:
            return 0
        for i in range(len(blocks)-k+1):
            color_block = blocks[i: i+k]
            count = min(count, color_block.count("W"))
        return count


x = Solution()
blocks = "WBBWWBBWBW"; k = 7
if x.minimumRecolors(blocks, k) == 3:
    print("Passed 1")

blocks = "WBWBBBW"; k = 2
if x.minimumRecolors(blocks, k) == 0:
    print("Passed 2")
