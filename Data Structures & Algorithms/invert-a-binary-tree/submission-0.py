# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
            
        todo = [root]
        
        while todo:
            node = todo.pop()
            # print(node)
            if node.left and not node.right:
                node.right = node.left
                node.left = None
                todo.append(node.right)
            elif node.right and not node.left:
                node.left = node.right
                node.right = None
                todo.append(node.left)
            elif node.right and node.left:
                left = node.left
                node.left = node.right
                node.right = left
                todo.append(node.left)
                todo.append(node.right)
        return root
        



        