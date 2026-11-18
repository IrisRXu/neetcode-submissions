class Solution:
    def climbStairs(self, n: int) -> int:
        # self.res = 0
        mem = {}
        
        def sol(stairs):
            if stairs == 0:
                return 1
            elif stairs < 0:
                return 0
            
            if stairs in mem:
                return mem[stairs]

            mem[stairs] = sol(stairs - 1) + sol(stairs - 2)
            return mem[stairs]

        sol(n)
        return mem[n]

            