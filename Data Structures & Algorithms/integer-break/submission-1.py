class Solution:
    def integerBreak(self, n: int) -> int:
        # Given an integer n, break it into a sum of at least 2 pos integers
        # and maximize the product of those integers
        # Return the maximum product can get
        dp = {}
        def breakInt(n):
            if n in dp:
                return dp[n]
            
            res = n
            for num in range(1, n + 1):
                res = max(res, num * breakInt(n - num))
            
            dp[n] = res
            return res
        
        # the bare minimum product is (n - 1) * 1 since n - 1 + 1 = n
        res = (n - 1)
        # since we need to ensure we have at least 2 integers in our sum
        # the first number cannot be the n itself ever
        for num in range(1, n):
            res = max(res, num * breakInt(n - num))
        
        return res