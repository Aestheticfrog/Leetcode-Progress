class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        adj = defaultdict(list)
        for u,v in roads:
            adj[u].append(v)
            adj[v].append(u)
        self.res = 0
        def dfs(n,p):
            tp = 1
            for x in adj[n]:
                if x != p:
                    tp += dfs(x,n)
            if n != 0:
                self.res += math.ceil(tp / seats)
            return tp
        dfs(0,-1)
        return self.res

