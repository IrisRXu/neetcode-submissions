class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mydict = {}
        for i, a in enumerate(nums):
            diff = target - a
            if diff in mydict:
                out = [mydict[diff],i]
                return out
            mydict[a] = i