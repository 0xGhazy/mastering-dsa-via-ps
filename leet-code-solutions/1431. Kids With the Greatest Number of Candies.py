# URL: https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        my_result = []
        max_candy = max(candies)
        
        for candy in candies:
            if candy + extraCandies >= max_candy:
                my_result.append(True)
            else:
                my_result.append(False)
                
        return my_result