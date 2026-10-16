class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # given an int arr prices of where prices[i] is the price of NeetCoin on the ith day
        # You can buy and sell one NeetCoin multiple times with the following restrictions:
            # After you sell your neetCoin, you cannot buy another one on the next day
            # You may only own at most one NeetCoin at a time
        # Return the maximum profit you can achieve

        # Naive alg
        # for every price we treat it as if we are buy it
            # Then we iterate through prices to the right of where we are, looking to sell wherever we would make a positive profit
                # Every time we find a sell price:
                    # We sell right there and then recurse the same process for 

        # we start at 
        n = len(prices)
        # dp[(price1, buy) = max Profit from buy/selling from price1 
        dp = {}

        # if we are buying, price is the price we sold at
        # if we are selling, price is the price we bought at
        def profit(idx, price, buy):
            # bounds check
            if idx >= len(prices):
                return 0


            res = 0
            if buy:
                # print(idx, price, "buy")
                for buyIdx in range(idx, len(prices)):
                    # check if we have bought from this buyIdx b4
                    if (buyIdx, buy) not in dp:
                        res = max(res, -prices[buyIdx] + profit(buyIdx + 1, prices[buyIdx], False))
                    else:
                        res = max(res, dp[(buyIdx, buy)])
            else: # we are selling
                # print(idx, price, "sell")
                for sellIdx in range(idx, len(prices)):
                    # only want positive profit
                    if prices[sellIdx] <= price:
                        continue
                    # check if we have sold this sellIdx b4
                    if (sellIdx, buy) not in dp:
                        res = max(res, prices[sellIdx] + profit(sellIdx + 2, prices[sellIdx], True))
                    else:
                        res = max(res, dp[(sellIdx, buy)])

            dp[(idx, buy)] = res
            return res


        
        return profit(0, 0, True)
