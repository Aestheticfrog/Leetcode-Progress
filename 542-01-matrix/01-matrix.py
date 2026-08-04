class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        if not mat or not mat[0]:
            return []
        m,n = len(mat),len(mat[0])
        q = deque()
        mv = m * n
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    q.append((i,j))
                else:
                    mat[i][j] = mv
        direc = [(1,0),(0,1),(-1,0),(0,-1)]
        while q:
            r, c = q.popleft()
            for dr, dc in direc:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and mat[nr][nc] > mat[r][c] + 1:
                    mat[nr][nc] = mat[r][c] + 1
                    q.append((nr, nc))
        return mat