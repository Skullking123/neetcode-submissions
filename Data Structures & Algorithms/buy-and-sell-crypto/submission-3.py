class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        
        buy = prices[0]
        res = 0

        for sell in prices:
            res = max(res, sell - buy)

            if sell < buy:
                buy = sell
        
        return res

        
            
