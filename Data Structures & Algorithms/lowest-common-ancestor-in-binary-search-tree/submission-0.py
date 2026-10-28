# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        ancestorsP = []
        ancestorsQ = []

        curr = root

        while curr and curr.val != p.val:
            ancestorsP.append(curr)
            if curr.val > p.val:
                curr = curr.left
            else:
                curr = curr.right

        ancestorsP.append(curr)
        
        curr = root

        while curr and curr.val != q.val:
            ancestorsQ.append(curr)
            if curr.val > q.val:
                curr = curr.left
            else:
                curr = curr.right

        ancestorsQ.append(curr)

        for i in reversed(range(0, min(len(ancestorsP), len(ancestorsQ)))):
            if ancestorsP[i].val == ancestorsQ[i].val:
                return ancestorsP[i]


        