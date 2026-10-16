class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # gas[i] is the amount of gas at the ith gas station
        # cost[i] is the amount of gas needed to travel from the ith station to the (i + 1) station
            # last station is connected to the first station (circular)
        # return the starting gas station's index such that you can travel around the circuit clockwise


        # greedy algs need a short-term heuristic 
        # start at the gas station with the most gas?
        # the only gas stations that can be starts are gas stations that have enough gas to get to the very next
        # in order to make a full rotation around the circuit, there must be sum(cost) gas available
        # 
        n = len(gas)

        if sum(cost) > sum(gas):
            return -1

        tank = 0
        res = 0
        for idx in range(n):
            tank += gas[idx]
            if cost[idx] > tank:
                tank = 0
                res = (idx + 1) % n
            else:
                tank -= cost[idx]
        
        return res
        