class Solution:
    def numSquares(self, n: int) -> int:
        # Given an integer n, return the least number of perfect
        # square numbers that sum to n.
        
        maxBase = math.floor(n**(1/2))
        queue = deque()
        queue.append(0)
        seen = set()
        dist = 0
        while queue:
            for _ in range(len(queue)):
                curr = queue.popleft()

                # the first time we see n, is when we find the shortest path
                if curr == n:
                    return dist
                
                # don't repeat computations
                if curr in seen:
                    continue
                
                seen.add(curr)

                for base in range(maxBase + 1):
                    queue.append(curr + (base * base))
        
            dist += 1
