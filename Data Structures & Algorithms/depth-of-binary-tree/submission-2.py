# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    # counter = 0
    # res = 0
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

        # q = deque()
        # counter = 0

        # if root:
        #     q.add(root.val)
        #     counter += 1
        
        # while q:
        #     node = q.popleft()
        #     if node.left:
        #         q.add(node.left)
        #     if node.right:
        #         q.add(node.right)




        
        


        

        