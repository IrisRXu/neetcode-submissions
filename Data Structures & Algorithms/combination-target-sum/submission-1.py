class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        curr = []
        list.sort(nums, reverse = True)

        def sol(res, curr, i):
            if sum(curr) == target:
                res.append(curr.copy())
                return
            elif sum(curr) > target or i == len(nums) or nums[i] > target:
                return
            
            idx = i+1
            # print(curr)
            # sol(res,curr,idx)
            
            for _ in range(0, target//nums[i]):
                curr.append(nums[i])
                # print(curr)
                sol(res,curr,i+1)
            for _ in range(0, target//nums[i]):
                curr.pop()

            sol(res,curr,i+1)

        sol(res, curr, 0)
        return res



