# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = collections.deque()

        if root:
            q.append(root)

        res = []

        while q:
            l = len(q)
            print(l)
            if q[-1]:
                res.append(q[-1].val)
                print(res)
            for i in range(l):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                
                    
        return res

