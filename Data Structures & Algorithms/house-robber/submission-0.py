class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        mem = {}

        def sol(i):
            if i >= n:
                return 0

            if i in mem:
                return mem[i]

            mem[i] = max(sol(i+2) + nums[i], sol(i+1))

            return mem[i]

        return sol(0)
