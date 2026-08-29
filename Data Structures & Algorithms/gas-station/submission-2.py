class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        res = 0
        i = 1
        tank = gas[res]
        while i < len(gas):
            if i == res:
                break

            tank -= cost[i-1]
            if tank < 0:
                tank = 0
                res = i
            tank += gas[i]
            i += 1
            if i >= len(gas):
                i = 0
        return res