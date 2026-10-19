class Solution:
    def hammingWeight(self, n: int) -> int:
        # Return the number of 1 bits in its binary
        ones = 0
        bitmask = 1

        for _ in range(32):
            if n & bitmask > 0:
                ones += 1
            bitmask <<= 1

        return ones