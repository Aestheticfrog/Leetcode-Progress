class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0
        r = len(grid)
        c = len(grid[0])
        res = 0
        def dfs(x,y):
            if x < 0 or y < 0 or x >= r or y >= c or grid[x][y] == "0":
                return
            grid[x][y] = "0"
            dfs(x - 1,y)
            dfs(x + 1,y)
            dfs(x,y - 1)
            dfs(x,y + 1)
        for x in range(r):
            for y in range(c):
                if grid[x][y] == "1":
                    res += 1
                    dfs(x,y)
        return res