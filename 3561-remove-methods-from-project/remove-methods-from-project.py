class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(n)]
        for u,v in invocations:
            adj[u].append(v)
        q = deque()
        q.append(k)
        visited = [0] * n
        while q:
            cur = q.popleft()
            visited[cur] = 1
            for negh in adj[cur]:
                if not visited[negh]:
                    q.append(negh)
        res = []
        for u, v in invocations:
            if not visited[u] and visited[v]:
                return list(range(n))
        for i in range(n):
            if not visited[i]:
                res.append(i)
        return res