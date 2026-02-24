class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        net = [gas[i] - cost[i] for i in range(len(gas))]
        
        total = 0
        tank = 0 
        start = 0 
        
        i = 0 
        while i < len(gas): 
            total += net[i]
            tank += net[i]
            if tank < 0: 
                start = i + 1 
                tank = 0
           
            i += 1 
        
        if total < 0: 
            return -1
        else: 
            return start



