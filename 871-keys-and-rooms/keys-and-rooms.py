class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        q = [0]
        visited = [0] * len(rooms)
        visited[0] = 1
        while q:
            cur = q.pop()
            for n in rooms[cur]:
                if visited[n] == 0:
                    visited[n] = 1
                    q.append(n)
        for i in range(len(rooms)):
            if visited[i] == 0:
                return False
        return True