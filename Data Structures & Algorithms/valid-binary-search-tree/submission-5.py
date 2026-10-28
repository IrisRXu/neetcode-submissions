# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.res = True
        self.maxv = -1000000001

        def dfs(curr):
            if not curr:
                return

            dfs(curr.left)
            print(curr.val, self.maxv)
            if curr.val > self.maxv:
                self.maxv = curr.val
            else:
                self.res = False
                return

           

            # if curr.left:
            #     if curr.left.val <= minv or curr.left.val >= curr.val:
            #         self.res = False
            #         return
            # if curr.right:
            #     if curr.right.val >= maxv or curr.right.val <= curr.val:
            #         self.res = False
            #         return
            dfs(curr.right)

        dfs(root)

        return self.res
