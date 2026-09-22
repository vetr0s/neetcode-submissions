class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        ROWS, COLS = len(grid), len(grid[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def bfs(sr, sc):
            q = collections.deque([(sr, sc)])
            grid[sr][sc] = "0"
            while q:
                r, c = q.popleft()
                for dx, dy in dirs:
                    nr, nc = r + dx, c + dy
                    if (0 <= nr < ROWS and
                        0 <= nc < COLS and
                        grid[nr][nc] == "1"):
                        q.append((nr, nc))
                        grid[nr][nc] = "0" 

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1":
                    bfs(i, j)
                    islands += 1
        return islands