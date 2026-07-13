class Solution:
    def fib(self, n: int) -> int:
        dp = {}

        def dfs(i):
            if i <= 0:
                return 0
            
            if i == 1:
                return 1

       
            dp[i] = dfs(i - 1) + dfs(i - 2)
            return dp[i]
        
        return dfs(n)