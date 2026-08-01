class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        for u,v in prerequisites:
            if [v,u] in prerequisites:
                return False
            else:
                adj[v].append(u)
                indegree[u] += 1
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        res = 0
        while q:
            cur = q.popleft()
            res += 1
            for n in adj[cur]:
                indegree[n] -= 1
                if indegree[n] == 0:
                    q.append(n)
        return res == numCourses
        