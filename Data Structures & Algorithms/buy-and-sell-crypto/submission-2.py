class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxRight = [0] * len(prices)
        maxRight[len(prices) - 1] = prices[len(prices) - 1] # init the last value as the last value of prices

        for index in range(len(prices) - 2, -1, -1):
            if prices[index] > maxRight[index + 1]:
                maxRight[index] = prices[index]
            else:
                maxRight[index] = maxRight[index + 1]
            # print(maxRight)

        profit = 0
        for index in range(len(prices)):
            profit = max(profit, maxRight[index] - prices[index])

        return profit
        
            
