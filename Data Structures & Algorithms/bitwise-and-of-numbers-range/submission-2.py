class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        # given two ints left and right
        # return the bitwise AND of all numbers in the range [left, right] inclusive

        # If for any bit position i:
            # There is at least one number in [left, right] at has a 0 at position i,
                # Then the end result will have 0 at position i
            # Otherwise, the end result will have a 1 at position i
        
        # Is it better to check if there is a number with 0 at position i

        # For the ith position bit
        # The numbers that have the ith position as 1 alternate
        # For example, when i = 2 (corresponding to 4), 
            # the four numbers 0,1,2,3 will have a 0 for their i = 2 bit
            # the next four numbers: 4,5,6,7 will have a 1 for their i = 2 bit
            # repeat
        # this can be generalized to:
        # For the ith position (corresponding to 2^i)
            # The first numbers 2^i numbers starting at and including 0, will have a 0 for their ith bit
            # The next 2^i numbers will have a 1 for their i = 2 bit
            # repeat
        res = 0
        bitmask = 1
        for power in range(32): 
            bitmask = 2**(power)
            # print(power, bitmask)

            # left has a 0 in the ith bit place, then res will have a 0
            # in the ith place too
            if left & bitmask == 0:
                # print(f"{power}th bit kept 0")
                continue
            
            # left has a 1 in the ith bit pos,
            # we need to check if we are able to reach a number with a 0 in the ith bit

            # calculate the smallest number that has a 0 in the ith pos that is in the [left, right] range
            num_with_zero_bit = ((left // bitmask) + 1) * bitmask
            # print(f"num_with_zero_bit: {num_with_zero_bit}")
            if right >= num_with_zero_bit:
                # print(f"{power}th bit kept 0")
                continue
            
            # we have determined that there is no number in [left, right] that has a 0
            # at the ith bit
            # print(f"{power}th bit turned to 1")
            res |= bitmask

        print(bin(res))
        return res
            


