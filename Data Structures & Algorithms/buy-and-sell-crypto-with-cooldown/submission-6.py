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
        def profit(idx, buy):
            # bounds check
            if idx >= len(prices):
                return 0

            if (idx, buy) in dp:
                return dp[(idx, buy)]

            cooldown = profit(idx + 1, buy)
            if buy:
                buying = profit(idx + 1, not buy) - prices[idx]
                dp[(idx, buy)] = max(cooldown, buying)
            else: # we are selling
                selling = profit(idx + 2, not buy) + prices[idx]
                dp[(idx, buy)] = max(cooldown, selling)

            return dp[(idx, buy)]

        
        return profit(0, True)
