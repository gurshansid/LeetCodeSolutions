class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        answer = 0
        
        while r < len(prices):
            if prices[r] < prices[l]:
                l = r
                r += 1
            else:
                answer = max(answer, prices[r] - prices[l])
                r += 1
        return answer
