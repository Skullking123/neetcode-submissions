class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0 

        buy = 0
        sell = 0

        for idx in range(len(prices)):
            if prices[idx] < prices[buy]:
                buy = idx
                sell = idx
            elif prices[idx] > prices[sell]:
                sell = idx
            res = max(res, prices[sell] - prices[buy])
        
        return res

        
            
