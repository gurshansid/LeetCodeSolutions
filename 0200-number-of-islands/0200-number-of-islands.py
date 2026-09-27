class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return None
        
        ROWS = len(grid)
        COLS = len(grid[0])
        islands = 0
        visited = set()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def dfs(r, c):
            queue = deque()
            queue.append([r, c])
            visited.add((r, c))

            while queue:
                row, col = queue.popleft()

                for dr, dc in directions:
                    nr, nc = row + dr, col + dc

                    if (nr in range(ROWS) and nc in range(COLS) and grid[nr][nc] == "1" and (nr, nc) not in visited):
                        queue.append([nr, nc])
                        visited.add((nr, nc))
            

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in visited:
                    dfs(r, c)
                    islands += 1
        return islands