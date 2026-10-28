# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.res = True

        def dfs(currP, currQ):
            if not currP and not currQ:
                return
            
            if not currP or not currQ:
                self.res = False
                return
            
            if currP.val != currQ.val:
                self.res = False
                return

            dfs(currP.left, currQ.left)
            dfs(currP.right, currQ.right)
        
        dfs(p, q)

        return self.res
