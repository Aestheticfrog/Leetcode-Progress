from collections import deque
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj = [[] for _ in range(n)]
        for i,j in edges:
            adj[i].append(j)
            adj[j].append(i)
        visited = [0] * n
        q = deque()
        q.append(source)
        while q:
            cur = q.popleft()
            if cur == destination:
                return True
            if visited[cur] == 0:
                visited[cur] = 1
                for n in adj[cur]:
                    if visited[n] == 0:
                        q.append(n)
        return False     


