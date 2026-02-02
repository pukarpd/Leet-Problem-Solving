# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        self.sums = 0 
        self.targetSum = targetSum
        self.res = False
        def dfs(root): 
            if not root: 
                return  
            self.sums += root.val
            if not root.right and not root.left and self.sums == self.targetSum : 
                self.res = True
            dfs(root.left)
            dfs(root.right)
            self.sums -= root.val
        
        dfs(root)
        return self.res