# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        res = []
        l1 = deque()
        l2 = deque()

        currl = []

        if root:
            l1.append(root)

        while l1 or l2:
            while l1:
                # print(type(l1))
                node = l1.popleft()
                currl.append(node.val)
                if node.left:
                    l2.append(node.left)
                if node.right:
                    l2.append(node.right)

            res.append(currl)
            currl = []
            l1 = l2
            l2 = deque()

        return res




        