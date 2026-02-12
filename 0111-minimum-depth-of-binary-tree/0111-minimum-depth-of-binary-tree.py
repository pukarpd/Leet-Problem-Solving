# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root: 
            return 0
        self.minDepth = float("inf")

        def dfs(root, depth): 
            if not root:
                return
            depth += 1 
            dfs(root.left, depth)
            dfs(root.right, depth)
            if not root.left and not root.right:
                self.minDepth = min(depth, self.minDepth)
            depth -=1 
            
        dfs(root, 0)

        return self.minDepth