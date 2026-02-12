# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        self.myset = set()
        def dfs(root): 
            if not root: 
                return 
            
            dfs(root.left)
            dfs(root.right)
            self.myset.add(root.val)
        dfs(root)
        print(len(self.myset))
        return True if len(self.myset) == 1 else False