class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        left = 0
        answer = 0

        for i in range(len(prices)):
            totalProfit = prices[i] - prices[left]

            answer = max(answer, totalProfit)

            if prices[i] < prices[left]:
                left = i
        
        return answer

