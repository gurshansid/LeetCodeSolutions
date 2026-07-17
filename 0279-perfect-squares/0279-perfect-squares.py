class Solution:
    def numSquares(self, n: int) -> int:
        dp = [n + 1] * (n + 1)
        dp[0] = 0

        for i in range(n + 1):
            square = 1

            while square * square <= i:
                dp[i] = min(dp[i], 1 + dp[i - square * square])

                square += 1
        
        return dp[n]
        