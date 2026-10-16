class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # given a list of flight tickets where tickets[i] = [from_i, to_i] represent the src airport and dest airport
        # Reconstruct the itinerary in order and return it
        # All of the tickets belong to someone who originally departed from "JFK". Reconstruct the flight path that 
            # the person too assuming each ticket is used exactly once
        # if there are multiple valid flight paths, return the lexicographically smallest one
        
        # first thought:
        # we treat every ticket as a unique directed edge
        # we dfs through the graph starting at JFK, marking edges that we take
            # at every node, we visit neighbors in lexicographic order priority
            # once we have utilized all the tickets, return the stack 

        # sort the list so that the destinations we will visit airports that are lexicographically 
        # smaller when we pop from the end of the adjacency list
        tickets.sort()
        
        # construct the adj list
        adj = defaultdict(deque)
        for from_i, to_i in tickets:
            adj[from_i].append(to_i)

        # keeps track of the itenerary we are building
        itenerary = []
        def dfs(airport):
            # we travel to this airport
            # print(airport)
            # print(itenerary)
            # used all tickets = complete itenerary 
            if len(itenerary) == len(tickets) + 1:
                return True
            
            # visit neighbors
            tickets_remaining = len(adj[airport])
            # in our current itenerary we only have tickets_remaining tickets left to leave this airport
            while adj[airport]:
                # get our next dest but also mark this edge as being used
                next = adj[airport].popleft()
                # if we had found a possible itenerary, propagate it
                if dfs(next):
                    return True
                # we are no longer using that edge rn, so put it back
                # adj[airport].append(next)
            # by the time we exit this loop, that means we haven't been able to make a complete itenerary yet
            # additionally, the queue should be back in the order it was before we traversed through it. 
            # Since we are pop from the left and then appending to the right when we come back. 

            # we have traversed all the possible paths with the tickets available to us, go back
            itenerary.append(airport)
            # we didn't find an itenerary
            return False
            
        dfs("JFK")
        itenerary.reverse()
        return itenerary
