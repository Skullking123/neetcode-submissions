class Solution:
    def countBits(self, n: int) -> List[int]:
        counts = []

        for num in range(n + 1):
            bitmask = 1
            count = 0
            for _ in range(32):
                if num & bitmask > 0:
                    count += 1
                bitmask <<= 1
            counts.append(count)
        
        return counts
        
        