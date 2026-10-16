class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # Given a 2-D integer arr points, where points[i] = [xi, yi]. Each point represents a 
        # distinct point on a 2-D plane
        # The cost of connecting two points is abs(xi - xj) + abs(yi - yj) for two points [xi, yi] and [xj, yj]
        # Return the minimum cost to connect all points together such that there exists exactly one path between each
        # pair of points

        # We are essentially returning all the sums of the minimum spanning tree
        # We can use PRIMs alg:
        # maintain a counter for the total sum of the edges of the mst we are building
        # maintain a visited set for the nodes we have touched
        # We iterate over the edges in order of the weights in asecending order:
            # if the edge is connects two nodes that we have already visited, then ignore
            # otherwise add the weight of the edge to our counter
            # keep going until we have visited all points
        if len(points) == 1:
            return 0
        
        heap = []
        adj = defaultdict(set)
        # start = (float('inf'), tuple(points[0]), tuple(points[1]))
        # get all the possible edges
        for p1 in range(len(points)):
            for p2 in range(p1 + 1, len(points)):
                if p1 == p2:
                    continue
                xi = points[p1][0]
                yi = points[p1][1]
                xj = points[p2][0]
                yj = points[p2][1]
                dist = abs(xi - xj) + abs(yi - yj)
                # if dist < start[0]:
                #     start = (dist, tuple(points[p1]), tuple(points[p2]))
                adj[tuple(points[p1])].add((dist, tuple(points[p2])))
                adj[tuple(points[p2])].add((dist, tuple(points[p1])))
                # print((dist, tuple(points[p1]), tuple(points[p2])))

        visited = set()
        cost = 0
        visited.add(tuple(points[0]))
        for edge in adj[tuple(points[0])]:
            heapq.heappush(heap, edge)


        while heap:
            # we have connected all the points
            if len(visited) == len(points):
                break
            
            # process this edge
            dist, dest = heapq.heappop(heap)

            # skip over since we have already connected these verticies
            if dest in visited:
                continue

            # print(dist)
            # add this edge to our spanning tree
            visited.add(dest)
            cost += dist

            # explore the new edges we can reach
            for weight, next in adj[dest]:
                adj[next].remove((weight, dest))
                if next in visited:
                    continue
                heapq.heappush(heap, (weight, next))
            


        return cost