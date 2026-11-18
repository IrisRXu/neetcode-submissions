class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        cand = sorted(candidates)
        # print(cand)
        res = []
        curr = []

        def sol(res,curr,i):
            if sum(curr) == target:
                # print(curr, res)
                res.append(curr.copy())
                return
            elif sum(curr) > target or i == len(cand):
                return

            curr.append(cand[i])
            # print(curr)
            sol(res,curr,i+1)
            curr.pop()
            
            while i+1 < len(cand) and cand[i] == cand[i+1]:
                i += 1
            # print(curr)
            sol(res,curr,i+1)


        sol(res,curr,0)
        return res 
            

        