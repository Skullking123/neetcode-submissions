class Solution:
    def getSum(self, a: int, b: int) -> int:
        # given two ints a and b, return the sum of the two integers 
        # without using the + and - operators

        # we must do bitwise operations
        # if a[i] = 0 and b[i] = 1, then res[i] = 1
        # if a[i] = 1 and b[i] = 1, then res[i] = 0 and need to carry the 1 to the next
        # There are at most 32 bits in an int
        res = 0
        carryOver = 0
        bitmask = 1 
        if b > a:
            a, b = b, a

        for offset in range(32):
            
            # get the bits
            a_bit = a & bitmask
            b_bit = b & bitmask  
            # print(a_bit, b_bit)
            # copy the result into res
            res |= (a_bit ^ b_bit ^ carryOver)

            bitmask <<= 1
            # we only have carryover if both a_bit and b_bit are 1's
            if (a_bit > 0 and b_bit > 0) or (a_bit > 0 and carryOver > 0) or (b_bit > 0 and carryOver > 0):
                carryOver = bitmask
            else:
                carryOver = 0

        if res > 0x7FFFFFFF:
            res = ~(res ^ 0xFFFFFFFF)

        return res
    
    