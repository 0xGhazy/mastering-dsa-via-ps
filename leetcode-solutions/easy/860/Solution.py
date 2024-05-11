from typing import List

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change_list = [0, 0, 0]
        for bill in bills:
            if bill == 5:
                change_list[0] += 1
            elif bill == 10:
                change_list[1] += 1
                if change_list[0] > 0:
                    change_list[0] -= 1
                else:
                    return False
            elif bill == 20:
                change_list[2] += 1
                if change_list[1] >  0 and change_list[0] > 0:
                    change_list[1] -= 1
                    change_list[0] -= 1
                elif change_list[0] >= 3:
                        change_list[0] -= 3
                else:
                    return False
        return True


x = Solution()
print(x.lemonadeChange([5,5,5,10,20])==True)
print(x.lemonadeChange([5,5,10,10,20])==False)
print(x.lemonadeChange([5,5,10,20,5,5,5,5,5,5,5,5,5,10,5,5,20,5,20,5])==True)
print(x.lemonadeChange([5,5,5,10,5,5,10,20,20,20])==False)