# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        def bfs(root): 
            if not root: 
                return []
            dq = deque([root])
            res = []
            while dq: 
                lvl = [] 
                for _ in range(len(dq)): 
                    node = dq.popleft()
                    lvl.append(node.val)
                    if node.left: 
                        dq.append(node.left)
                    if node.right: 
                        dq.append(node.right)
                res.append(lvl)
            return res
        temp = bfs(root)
        res = []
        for x in temp: 
            res.append(x[-1])
        return res