class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # given an int arr of coins, representing coins of different denominations 
        # and an integer amount representing a target amount of money
        # return the number of distinct combinations that total up to amount. If it'simpossible to make up the amount, return 0
        
        # maintain a 2d dp arr
        # dp[coinIdx][amount] = # of combinations to get amount using coins at idx 0 to coinIdx
        # for every coin value:
            # for every amount from coin value to amount inclusive
                # we calculate the amount the total number of combinations to get to amount by using the current coin value
                    # this is equal to sum of 
                        # combinations that lead up to this amount using the prior coins 
                        # combinations that lead up to this amount using this coin. dp[coinIdx][amount - coinVal]
        
        # represents the number of combinations to get to amount using all the coins
        # return dp[-1][-1]



        n = len(coins)
        # dp[coinIdx][amount] = # of combinations to get amount using coins at idx 0 to coinIdx
        dp = [[0] * (amount + 1) for i in range(n)]

        # intitalize the base cases
        factor = 0
        while coins[0] * factor <= amount:
            subAmt = coins[0] * factor
            dp[0][subAmt] = 1
            factor += 1


        for idx in range(1, n):
            dp[idx][0] = 1
            value = coins[idx]
            for subAmt in range(1, amount + 1):
                dp[idx][subAmt] = dp[idx - 1][subAmt] + dp[idx][subAmt - value]
        
        # print(dp)
        return dp[n - 1][amount]

        

