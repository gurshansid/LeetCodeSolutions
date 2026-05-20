class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        pointer = 0

        for i in range(len(prices)):
            if prices[i] < prices[pointer]:
                pointer = i
                
            profit = prices[i] - prices[pointer]
            result = max(result, profit)
        
        return result