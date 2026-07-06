class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost) 
        mem = [0]*(n+2)

        for i in range(n-1, -1, -1):
            mem[i] = cost[i] +  min(mem[i+1], mem[i+2])
        return min(mem[0], mem[1]) 