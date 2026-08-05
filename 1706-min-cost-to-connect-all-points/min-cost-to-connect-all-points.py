class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        min_heap = [(0,0)]
        visited = set()
        res = 0
        while len(visited) < n:
            c,u = heapq.heappop(min_heap)
            if u not in visited:
                visited.add(u)
                res += c
                x1 , y1 = points[u]
                for v in range(n):
                    if v not in visited:
                        x2 , y2 = points[v]
                        dist = abs(x1 - x2) + abs(y1 - y2)
                        heapq.heappush(min_heap,(dist,v))
        return res