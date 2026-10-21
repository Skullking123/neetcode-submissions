class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # There is a car with capacity empty seats
            # The car can only drive east
        # Given an integer array trips where trips[i] = [numPassengers[i], from[i], to[i]]
        # A trips[i] has numPassengers[i] that need to get to to[i] from from[i]
        # Return true if it is possible to pick up and drop off all passengers for all the given trips
        # False otherwise

        # In order to get all passengers to their dest, we need be able to
        # see if we have enough capacity in the car at the time we arrive at their stop
        # This is because we are only able to head east, so we cannot revisit stops to pick 
        # up passengers that we had missed

        # Sort the trips in order of when we are visiting
        trips.sort(key=lambda x : (x[1], x[2]))
        
        # elms = (dest, num_pass_to_drop_off_at_dest)
        drop_off = []
        pass_in_car = 0
        for psgrs, src, dest in trips:
            # subtract the number of passengers we have dropped off since the last stop
            while drop_off and drop_off[0][0] <= src:
                # we have alr dropped off the passengers
                pass_in_car -= drop_off[0][1]
                heapq.heappop(drop_off)
            
            # pickup the passengers at this stop
            pass_in_car += psgrs

            # exceeded capacity
            if pass_in_car > capacity:
                return False

            # add their stop 
            heapq.heappush(drop_off, (dest, psgrs))

        return True


