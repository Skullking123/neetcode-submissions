class Solution:
    def tribonacci(self, n: int) -> int:
        seq = [0,1,1]

        def helper(n):
            if n < len(seq):
                return seq[n]
            
            nth = helper(n - 1) + helper(n - 2) + helper(n - 3)
            seq.append(nth)
            return nth
        
        return helper(n)