class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        def helper(u,v):
            if u == v:
                return True
            visited.add(u)
            for n in graph[u]:
                if n not in visited:
                    if helper(n,v):
                        return True
            return False
        for u,v in edges:
            visited = set()
            if helper(u,v):
                return [u,v]
            graph[u].append(v)
            graph[v].append(u)
        return None