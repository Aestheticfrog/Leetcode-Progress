class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows , cols = len(grid),len(grid[0])
        fresh = 0
        q = deque()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    q.append((i,j))
                elif grid[i][j] == 1:
                    fresh += 1
        res = 0
        direc = [(1,0),(-1,0),(0,1),(0,-1)]
        while q and fresh > 0:
            res += 1
            for _ in range(len(q)):
                dr , dc = q.popleft()
                for r,c in direc:
                    nr = dr + r
                    nc = dc + c
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        q.append((nr,nc))
        if fresh == 0:
            return res
        else:
            return -1