# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        if not root: 
            return None 

        this = root

        while this: 
            if this.val < val: 
                this = this.right
            elif this.val > val: 
                this = this.left
            else: 
                break
        
        return this
