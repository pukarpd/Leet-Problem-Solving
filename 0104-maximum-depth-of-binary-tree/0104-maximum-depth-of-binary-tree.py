# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
    
        if root == None: 
            return 0

        nodecount = 0
        maxnodecount = 0
        val = [] 

        def dfs (node): 
            if node == None: 
                return 0

            nonlocal nodecount
            nonlocal maxnodecount 
            nonlocal val

            val.append(node.val)
            nodecount +=1

            print(nodecount)
            dfs(node.left) 
            dfs(node.right)
            
            if node.left == None and node.right == None: 
                maxnodecount = max(nodecount, maxnodecount)

            if node.val in val: 
                val.pop()
                nodecount -= 1 

           
                # print(nodecount) 
           
            
        
        dfs(root)
        return maxnodecount

