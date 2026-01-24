# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        self.seq = [] 

        def dfs(root): 
            if not root:
                return None
            dfs(root.left)
            dfs(root.right)

            if root.left == None and root.right == None: 
                self.seq.append(root.val)


        dfs(root1)
        r1cmp = copy.deepcopy(self.seq)
        self.seq = []
        dfs(root2)

        return r1cmp == self.seq
        