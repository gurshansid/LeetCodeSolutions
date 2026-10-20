class Solution:
    def longestIncreasingPath(self, matrix: list[list[int]]) -> int:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        longestPath = 0
        memo = {}


        def dfs(r, c):
            if (r, c) in memo:
                return memo[(r, c)]

            longest = 1
            
            if (r, c) in memo:
                return memo[(r, c)]
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if nr in range(ROWS) and nc in range(COLS) and matrix[nr][nc] > matrix[r][c]:
                    longest = max(longest, 1 + dfs(nr, nc))
            
            memo[(r, c)] = longest

            return longest
        
        for r in range(ROWS):
            for c in range(COLS):
                longestPath = max(longestPath, dfs(r, c))

        return longestPath

            

