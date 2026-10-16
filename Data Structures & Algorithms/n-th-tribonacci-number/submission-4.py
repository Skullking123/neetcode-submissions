class Solution:
    def tribonacci(self, n: int) -> int:
        tn_m3 = 0
        tn_m2 = 1
        tn_m1 = 1

        # base cases
        if n == 0:
            return tn_m3
        elif n == 1:
            return tn_m2
        elif n == 2:
            return tn_m1
        
        for n in range(3, n + 1):
            temp = tn_m1 + tn_m2 + tn_m3
            tn_m3 = tn_m2
            tn_m2 = tn_m1
            tn_m1 = temp
        
        return tn_m1