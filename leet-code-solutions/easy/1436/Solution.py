from typing import List

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        paths_dict = self.map_to_dict(paths)
        for i in paths_dict.values():
            if i not in paths_dict.keys():
                return i

                
    def map_to_dict(self, paths: List[List[str]]) -> dict:
        result = {}
        for path in paths:
            result[path[0]] = path[1]
        return result

        



x = Solution()
print(x.destCity([["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]) == "Sao Paulo" )
print(x.destCity([["B","C"],["D","B"],["C","A"]]) == "A" )
print(x.destCity([["A","Z"]]) == "Z" )