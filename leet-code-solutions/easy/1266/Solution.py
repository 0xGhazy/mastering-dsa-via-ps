class Solution:
    def minTimeToVisitAllPoints(self, points: list[list[int]]) -> int:
        cost = 0
        for i in range(len(points)):
            if i + 1 <= len(points) - 1:
                src, dist = points[i], points[i+1]
                temp_dist = [dist[0] - src[0], dist[1] - src[1]]
                if temp_dist[0] == temp_dist[1]:
                    cost += abs(temp_dist[0])
                else:
                    max_num = max([abs(temp_dist[0]), abs(temp_dist[1])])
                    cost += max_num
        return cost

x = Solution()
points = [[1,1],[3,4], [-1,0]]
if x.minTimeToVisitAllPoints(points) == 7:
    print("Passed")

points = [[3,2],[-2,2]]
if x.minTimeToVisitAllPoints(points) == 5:
    print("Passed")