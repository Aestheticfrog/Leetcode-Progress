class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = list(range(n + 1))
        def find(u):
            if parent[u] != u:
                parent[u] = find(parent[u])
            return parent[u]
        for u,v in edges:
            t1 = find(u)
            t2 = find(v)
            if t1 == t2:
                return [u,v]
            parent[t1] = t2
        return []