class Solution:
    def mySqrt(self, x: int) -> int:
        # Given a non-negative int x, return the sqrt of x rounded down to the nearest int
        # You cannot use any built-in exponent function or operator

        # Use binary search and search between all values between 0 and x inclusive
        # If there is an exact root, binary search will find it 
        # But if there isn't just save the root whose root^2 has the smallest pos diff from x
        left = 0
        right = x
        
        diff = float('inf')
        res = 0
        while left <= right:
            mid = (left + right) // 2
            
            squared = mid * mid
            # 
            if x - squared > 0 and x - squared < diff:
                diff = x - squared
                res = mid

            if squared < x:
                left = mid + 1
            elif squared > x:
                right = mid - 1
            else: # when mid * mid == x
                return mid
        
        return res