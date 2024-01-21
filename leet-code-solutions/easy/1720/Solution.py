class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        result = [first]
        for i in encoded:
            result.append(result[-1] ^ i)
        return result