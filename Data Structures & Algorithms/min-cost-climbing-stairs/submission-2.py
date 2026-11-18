class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        mem = {}

        def sol(s):
            if s == 0 or s == 1:
                return 0
            
            if s in mem:
                return mem[s]

            mem[s] = min(sol(s-1) + cost[s-1], sol(s-2) + cost[s-2])
            
            return mem[s]

        return sol(n)


        
