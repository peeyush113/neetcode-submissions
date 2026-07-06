class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost) 
        j, k = 0, 0

        for i in range(n-1, -1, -1):
            j, k = cost[i] +  min(j, k), j
        return min(j, k) 