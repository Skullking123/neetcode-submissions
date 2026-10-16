class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        store = [amount + 1] * (amount + 1)
        store[0] = 0



        for sub in range(1, amount + 1):
            for coin in coins:
                if sub - coin >= 0:
                    res = 1 + store[sub - coin]
                    store[sub] = min(res, store[sub])


        if store[amount] > amount:
            return -1
        else:
            return store[amount]