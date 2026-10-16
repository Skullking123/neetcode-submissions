class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # n = airports labeled 0 to n -1
        # Given an arr flights where flights[i] = [from_i, to_i, price_i] represents 
        # a one-way flight from airport from_i to airport to_i with cost price_i.
        # src = starting
        # dst = destination
        # src != dst
        # k is the maximum number of stops you can make
        queue = deque()
        adj = defaultdict(set)
        for dprt, arvl, cost in flights:
            adj[dprt].add((arvl, cost))
            if dprt == src:
                queue.append((dprt, arvl, cost))
                
        res = float('inf')
        prev = [float('inf')] * n
        prev[src] = 0
        for stop in range(k + 1):
            curr = prev.copy()
            # print(stop)
            for _ in range(len(queue)):
                dprt, arvl, cost = queue.popleft()
                # print((dprt, arvl, cost), curr[arvl], prev[dprt] + cost)  
                if prev[dprt] + cost < curr[arvl]:
                    curr[arvl] = prev[dprt] + cost
                    for next, cost in adj[arvl]:
                        queue.append((arvl, next, cost))
            # for dprt, arvl, cost in flights:
            #     if prev[dprt] == float('inf'):
            #         continue
            #     curr[arvl] = min(prev[dprt] + cost, curr[arvl])
            #     # print((dprt, arvl, cost), curr[arvl], prev[dprt] + cost)      
            # print(curr)           
            prev = curr
            # # print(prev)
        
        return prev[dst] if prev[dst] != float('inf') else -1