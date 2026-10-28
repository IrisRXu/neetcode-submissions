# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        self.res = False

        def dfs(curr, subRoot):
            if not curr:
                return
            if curr.val == subRoot.val:
                self.res = True
                sameTree(curr, subRoot)
                if self.res == True:
                    return

            dfs(curr.left, subRoot)
            dfs(curr.right, subRoot)
        
        def sameTree(curr, subRoot):
            
            if not curr and not subRoot:
                return

            # print(curr, subRoot)
            # if curr: print(curr.val)
            # if subRoot: print(subRoot.val)

            if not curr or not subRoot:
                self.res = False
                return
            if curr.val != subRoot.val:
                self.res = False
                return
                
            sameTree(curr.left, subRoot.left)
            sameTree(curr.right, subRoot.right)
                

        dfs(root, subRoot)

        return self.res

            
        