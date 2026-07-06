class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost) 
        mem = [0]*(n+2)

        for i in range(n-1, -1, -1):
            mem[i] = cost[i] +  min(mem[i+1], mem[i+2])
        print(mem)
        return min(mem[0], mem[1]) 


        mem = {}
        def dfs(i):
            if i >= len(cost):
                return 0
            if not i in mem:
                mem[i] = cost[i] + min(dfs(i+1), dfs(i+2))
            return mem[i]
        return min(dfs(0), dfs(1))