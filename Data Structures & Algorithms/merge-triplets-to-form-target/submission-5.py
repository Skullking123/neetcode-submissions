class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # given a list of triplets, return true if it is possible to get the target
        # The operations that you can do is:
            # Choose two different triples and update one of them to [max(ai, aj), max(bi, bj), max(ci, cj)]
        
        # we should automatically ignore any triplet that contains elements that are bigger than the elements of our target
        n = len(triplets)
        prev = 0
        while prev < n and (triplets[prev][0] > target[0] or triplets[prev][1] > target[1] or triplets[prev][2] > target[2]):
            prev += 1
        
        if prev >= n:
            return False

        for idx in range(1, n):
            a, b, c = triplets[idx]
            if a > target[0] or b > target[1] or c > target[2]:
                print(f"skipped {triplets[idx]}")
                continue
            print(f"Updated {triplets[idx]} to {self.updateTriplet(triplets[prev], triplets[idx])} with {triplets[prev]}")
            triplets[idx] = self.updateTriplet(triplets[prev], triplets[idx])
            prev = idx

        return triplets[prev] == target

    def updateTriplet(self, triplet1, triplet2):
        return [max(triplet1[0], triplet2[0]), max(triplet1[1], triplet2[1]), max(triplet1[2], triplet2[2])]


        #[[15,9,8],[2,4,4],[2,6,1],[10,9,4],[10,4,1],[2,12,11],[1,4,2],[15,1,14],[6,2,9],[4,5,11]]
        #[10,9,9] True