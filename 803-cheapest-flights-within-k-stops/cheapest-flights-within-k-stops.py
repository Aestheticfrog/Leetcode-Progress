class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = [[] for _ in range(n)]
        for u,v,w in flights:
            adj[u].append((v,w))
        dist = [float("inf")] * n
        dist[src] = 0
        q = deque()
        q.append((src,0,0))
        while q:
            node, cost, stop = q.popleft()
            if stop > k:
                continue
            for n,p in adj[node]:
                temp = cost + p
                if temp < dist[n]:
                    dist[n] = temp
                    q.append((n,temp,stop + 1))
        if dist[dst] == float("inf"):
            return -1
        return dist[dst]