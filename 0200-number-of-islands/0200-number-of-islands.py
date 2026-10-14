class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        answer = 0
        visited = set()

        def dfs(r, c):
            if r not in range(ROWS) or c not in range(COLS) or (r, c) in visited or grid[r][c] != "1":
                return 0
            
            visited.add((r, c))

            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                dfs(nr, nc)
            
            return 1
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in visited:
                    answer += dfs(r, c)
        return answer