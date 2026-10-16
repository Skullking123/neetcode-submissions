class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        # for each element, choose to either add or subtract it from the total
        # equivalent to partitioning into two lists, which is 2^n

        # however, we know that for partitioning elements from a list, we can optimize by using
        # the knapsack algorithm, which in this case, since we have to take whole elements is 0-1 knapsack

        # consider 1, 2, 3
        # we have a matrix of size sum(stones) + 1 x stones (m x n array)
        # s = sum(stones)
        # each location in the array is T/F
        
        # n = len(stones)  m = sum(stones)
        # O(m x n)
        # O(2 * m)
        # O(m)
        s = sum(stones)
        # memo = [[False] * (len(stones) + 1) for _ in range(sum(stones) + 1)]

        # memo[0][0] = True
        # prev[sum] = whether a partition of sum is possible
        med = s // 2
        prev = [False] * (med + 1)
        prev[0] = True
        for c in range(1, len(stones) + 1):
            curr = [False] * (med + 1)
            curr[0] = True
            for r in range(med + 1):
                if prev[r]:
                    curr[r] = True
                else:
                    print(c - 1)
                    if r - stones[c - 1] >= 0:
                        curr[r] = prev[r - stones[c - 1]]
            prev = curr

        # for l in memo:
        #     print(l)
        
        # even sum case
        print(prev)
        offset = 0
        if s % 2 == 0:
            r = med
            while True:
                if prev[r - offset]:
                    return offset * 2
                offset += 1
        # odd sum case
        else:
            r1 = med
            while True:
                print(offset)
                if prev[r1 - offset]:
                    return offset * 2 + 1
                offset += 1