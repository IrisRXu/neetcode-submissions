# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxHeight(self, node: Optional[TreeNode]):
        if not node:
            return 0
        return max(self.maxHeight(node.left), self.maxHeight(node.right)) + 1

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        # print(root.left)
        l = self.maxHeight(root.left)
        r = self.maxHeight(root.right)

        return max(self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right), l + r)

    
