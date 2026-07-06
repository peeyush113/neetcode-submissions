class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int: 
        j, k = 0, 0

        for i in range(len(cost)-1, -1, -1):
            j, k = cost[i] +  min(j, k), j
        return min(j, k) 