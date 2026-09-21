class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        rows, cols = len(grid), len(grid[0])
        islands = 0
        directions = [(1,0), (-1, 0), (0, 1), (0, -1)]

        def bfs(sr, sc):
            q = collections.deque([(sr, sc)])
            grid[sr][sc] = "0"
            while q:
                r, c = q.popleft()
                for dx, dy in directions:
                    nr, nc = r + dx, c + dy
                    if (0 <= nr < rows and
                        0 <= nc < cols and
                        grid[nr][nc] == "1"):
                        q.append((nr, nc))
                        grid[nr][nc] = "0"

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    bfs(r, c)
                    islands += 1
        
        return islands