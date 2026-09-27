class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        answer = 0
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]

        def bfs(r, c):
            size = 1
            queue = deque()
            queue.append((r, c))
            visited.add((r, c))

            while queue:
                row, col = queue.popleft()

                for dr, dc in directions:
                    nr, nc = row + dr, col + dc

                    if (nr in range(ROWS) and nc in range(COLS) and grid[nr][nc] == 1 and (nr, nc) not in visited):
                        queue.append((nr, nc))
                        visited.add((nr, nc))
                        size += 1
            return size


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r,c) not in visited:
                    answer = max(answer, bfs(r, c))
        return answer