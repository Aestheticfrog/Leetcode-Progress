class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        rev = [[] for _ in range(n)]
        indegree = [0] * n
        for u in range(n):
            for v in graph[u]:
                rev[v].append(u)
            indegree[u] = len(graph[u])
        q = deque([i for i in range(n) if indegree[i] == 0])
        safe = [0] * n
        while q:
            cur = q.popleft()
            safe[cur] = 1
            for j in rev[cur]:
                indegree[j] -= 1
                if indegree[j] == 0:
                    q.append(j)
        return [i for i in range(n) if safe[i] == 1]
