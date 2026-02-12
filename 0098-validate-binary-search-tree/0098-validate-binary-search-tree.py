# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # neetcode 
        def valid(node, left, right): 
            if not node: 
                return True 

            if not (left < node.val and node.val < right ): 
                return False 

            return (valid(node.left, left, node.val) and valid(node.right, node.val, right))

        return valid(root, float("-inf"), float("inf"))



        # because i did not understand question, bad architecture 
        # if not root: 
        #     return
        
        # isleftValid = False 
        # isrightValid = False   
        # if root.left: 
        #     if root.left.val < root.val: 
        #         isleftValid = True 
        #     else: 
        #         return False
        # else: 
        #     isleftValid = True 

        # if root.right: 
        #     if root.right.val > root.val: 
        #         isrightValid = True 
        #     else: 
        #         return False 
        # else: 
        #     isrightValid = True 

        # if isleftValid and isrightValid: 
        #     self.isValidBST(root.left)
        #     self.isValidBST(root.right)
        
        # return True 
