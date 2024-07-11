class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(cost) > sum(gas):
            return -1
        currentGas = 0
        ans=0
        for i in range(len(gas)):
            currentGas += gas[i] - cost[i]
            if currentGas < 0:
                currentGas = 0
                ans = i+1
        return ans
