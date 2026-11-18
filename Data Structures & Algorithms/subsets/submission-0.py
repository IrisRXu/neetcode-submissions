class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = []
        
        
        def sol (res, curr, i):
            if i == len(nums):
                res.append(curr.copy())
                return
            
            curr.append(nums[i])
            sol(res,curr,i+1)

            curr.pop()
            sol(res,curr,i+1)

        sol(res, curr, 0)
        return res
        

        
        