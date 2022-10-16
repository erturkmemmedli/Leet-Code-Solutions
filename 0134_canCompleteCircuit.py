class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        sum_gas = sum(gas)
        sum_cost = sum(cost)
        if sum_gas < sum_cost: return -1
        gas_current = gas[0]
        cost_current = cost[0]
        index = 0 if gas_current >= cost_current else -1
        for i in range(1, n):
            if gas_current < cost_current:
                gas_current = gas[i]
                cost_current = cost[i]
                index = i if gas_current >= cost_current else -1
            else:
                gas_current += gas[i]
                cost_current += cost[i]
        return index
