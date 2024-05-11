class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_gain, max_alt = 0, 0
        for i in gain:
            max_alt += i
            max_gain = max(max_alt, max_gain)
        return max_gain
