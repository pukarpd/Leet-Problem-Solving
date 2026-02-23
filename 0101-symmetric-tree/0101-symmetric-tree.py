# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        

        def dfsleft(root, arr): 
            if not root: 
                arr.append(None)
                return
            
            dfsleft(root.left, arr)
            dfsleft(root.right, arr)
            arr.append(root.val)

            return arr
        def dfsright(root, arr): 
            if not root: 
                arr.append(None)
                return
            
            dfsright(root.right, arr)
            dfsright(root.left, arr)
            arr.append(root.val)

            return arr

        left = dfsleft(root.left, [])
        right = dfsright(root.right, [])
        # print(left, right)

        return left == right