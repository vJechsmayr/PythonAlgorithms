""" 
134. Gas Station Problem 

Problem:-
There are N gas stations along a circular route, where the amount of gas at station i is gas[i].
You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1).
You begin the journey with an empty tank at one of the gas stations.
Return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1.

Input:- gas = [1,2,3,4,5], gas is the array consisting of the gas can get at i th stop
        cost= [3,4,5,1,2], cost is the array consisting of the cost to travel from i to i+1 index

Output:- 3, we have to return the index from where we can start journey and traverse all stops in clockwise manner

Time complexity :- O(N) where N is the number is the size of array(stops)
Space complexity:- O(1)

"""

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # total_fuel variable is maintained to check if path is possible or not if sum(gas) < sum(cost) return -1
        n = len(gas)
        curr_fuel = 0
        total_fuel = 0
        start_idx = 0
        
        for i in range(n):
            curr_fuel += gas[i]-cost[i]
            total_fuel += gas[i]-cost[i]
            # at any index if fuel becomes less than 0 then we have to choose new starting index
            if curr_fuel < 0:
                # start_idx will be i+1 because at i th index out curr_fuel became < 0
                # so we start from any index between start_idx and i there will be no valid start_idx
                start_idx = i+1
                # reset the curr_fuel to 0 as we have chose new start_idx
                curr_fuel = 0
        # at last check if start_idx is less than n and total_fuel is not less than 0 return start_idx else -1
        return start_idx if start_idx < n and total_fuel>=0 else -1


