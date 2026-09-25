class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        left = 0
        right = 0
        answer = 0

        while right < len(prices):
            profit = prices[right] - prices[left]
            answer = max(answer, profit)

            if prices[right] < prices[left]:
                left = right
            
            right += 1
        
        return answer
