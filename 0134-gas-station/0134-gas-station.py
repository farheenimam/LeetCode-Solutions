class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        gas_ttl = sum(gas)
        cost_ttl = sum(cost)

        if cost_ttl > gas_ttl:
            return -1
        current_gas = 0
        start = 0
        for i in range(0, len(gas)):
            current_gas += gas[i] - cost[i]
            if current_gas < 0:
                current_gas = 0
                start = i + 1
        return start    

        