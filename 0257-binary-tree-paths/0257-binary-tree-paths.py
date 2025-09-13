# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        if not root: 
            return  
        
        paths = []
        def getPath( root, path): 
            nonlocal paths
            if not root:
                return  

            path += str(root.val)
            if not root.left and not root.right: 
                paths.append(path)
                return

            
            path += "->"
            getPath(root.left, path)
            getPath(root.right, path)
            


            
        
        getPath(root, "")


        return paths


