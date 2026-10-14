class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        adj = {i:[] for i in range(numCourses)}
        visited = set()
        visiting = set()

        for c, p in prerequisites:
            adj[c].append(p)
         
        
        def dfs(c):
            if c in visited:
                return True
            
            if c in visiting:
                return False
            
            visiting.add(c)

            for nei in adj[c]:
                if not dfs(nei):
                    return False
            
            visiting.remove(c)
            visited.add(c)

            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        
        return True
