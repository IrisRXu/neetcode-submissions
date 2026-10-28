# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.counter = 0

        def dfs(curr, maxval):
            if not curr:
                return

            # print(curr.val)
            # print(maxval, curr.val)

            if curr.val >= maxval:
                # print('here')
                self.counter += 1
                maxval = curr.val

            
            dfs(curr.left, maxval)
            dfs(curr.right, maxval)

        dfs(root, -101)

        return self.counter

            
# 2
#  4
#  10 8
#     4



