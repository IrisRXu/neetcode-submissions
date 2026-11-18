class Solution:
    def rob(self, nums: List[int]) -> int:
        mem={}
        n = len(nums)

        def sol(i, first):
            if i >= n:
                return 0

            if (i,first) in mem:
                return mem[(i,first)]

            if i == 0:
                res = max(sol(i+2, True) + nums[i], sol(i+1, False))
            elif i == n-1:
                if not first:
                    return nums[i]
                else:
                    return 0
            else:
                res = max(sol(i+2, first) + nums[i], sol(i+1, first))     
            mem[(i,first)] = res
            return mem[(i,first)]

        
        res = sol(0, False)
        return res

        