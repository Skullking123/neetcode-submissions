class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # Can only finish at most k projects
        # w is the initial amount of capital you have
        # profits[i] = pure profit of project i
        # capital[i] = capital cost of project i
        # Return the maximum net profit you can make

        # inital thoughts
            # O(1) knapsack: We are sifting through subsets of projects
                # But we have two restrictions: k and w
                # 2D dp arr?
                # k x w? dp[k][w] = max profit you can make using two projects with w cost
                    # But how to prevent dupicating projects?
            # dfs: We either take on a project or don't
                # doesn't work because we need to be able to backtrack to previous projects
                # to see if we are able to afford them after having already done other projects
            
        
        # a min-heap, mapping projects to their costs
        cap_costs = []

        for proj in range(len(profits)):
            heapq.heappush(cap_costs, (capital[proj], proj))

        # keep track of how much capital we have        
        curr_cap = w
        # a max-heap, mapping affordable projects to their profits
        affordable_projs = []
        for _ in range(k):
            
            while cap_costs and cap_costs[0][0] <= curr_cap:
                _, proj = heapq.heappop(cap_costs)     
                heapq.heappush(affordable_projs, (-profits[proj], proj))
            
            if not affordable_projs:
                break

            profit, proj = heapq.heappop(affordable_projs)
            profit = abs(profit)

            curr_cap += profit

        return curr_cap     




















