class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        visited = set()
        maxArea = 0

        def dfs(r, c):
            area = 1
            if r not in range(ROWS) or c not in range(COLS) or (r, c) in visited or grid[r][c] != 1:
                return 0
            
            visited.add((r, c))

            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                area += dfs(nr, nc)
            return area

        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in visited and grid[r][c] == 1:
                    maxArea = max(maxArea, dfs(r, c))
        return maxArea