class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # weights[i] is the weight of the ith package
        # Each day, we load the ship with packages on the conveyor belt in the order they are given
        # It is not allowed to load weight more than the maximum wieght capacity of the ship
        # Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within days



        # s = sum(weights)
        # n = len(weights)
        # O(log(s) * n)
        left = max(weights)
        right = sum(weights)

        def canShipWithinDays(maxWeight):
            currLoad = 0
            daysToShip = 1
            for weight in weights:
                # impossible
                if weight > maxWeight:
                    return False
                # we can't exceed our maximum weight
                # make this package be shipped out the next day
                if currLoad + weight > maxWeight:
                    daysToShip += 1
                    currLoad = 0
                currLoad += weight
            
            return daysToShip <= days

        res = float('inf')
        # [0, 1, 2, 3, 4] [6,7,8,9]
        while left <= right:
            mid = (right + left) // 2
            # print(left, mid, right)
            if canShipWithinDays(mid):
                # print("lower")
                res = min(res, mid)
                right = mid - 1
            else:
                # print("higher")
                left = mid + 1

        return res
