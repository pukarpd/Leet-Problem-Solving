# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        self.maxPath = []
        self.gn = 0 
        def dfs(root): 
            if not root: 
                return 
            self.maxPath.append(root.val)
            maxval = max(self.maxPath)
            # print(maxval, self.maxPath)
            if root.val >= maxval: 
                self.gn += 1 
            # if self.maxPath and root.left == None and root.right == None: 
            #     self.maxPath.pop()
            dfs(root.left)
            dfs(root.right)
            if self.maxPath: 
                self.maxPath.pop()
        
        dfs(root)
        
        return  self.gn