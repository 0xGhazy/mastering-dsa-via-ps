class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        names = list(zip(names, heights))
        names.sort(key=lambda x: x[1], reverse=True)
        sorted_list = [x[0] for x in names]
        return sorted_list


x = Solution()
names = ["Mary","John","Emma"]; heights = [180,165,170]
print(x.sortPeople(names, heights) == ["Mary","Emma","John"])
names = ["Alice","Bob","Bob"]; heights = [155,185,150]
print(x.sortPeople(names, heights) == ["Bob","Alice","Bob"])