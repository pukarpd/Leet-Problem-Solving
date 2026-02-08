# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # cracking FAANG soln
        def dfs(root): 
            if not root: 
                return None
         
            if root == p or root == q: 
                return root
            
            l = dfs(root.left)
            r = dfs(root.right)

            if l and r: 
                return root
            else: 
                return l or r  

        return dfs(root)

        # flawed logic, multiple attempts few test cases solved, didnt solve a general case. 
        # if not root.left or not root.right: 
        #     return root

        # self.seenq = False 
        # self.seenp = False
        # self.lca_so_far = root
        # def dfs(root): 

        #     if not root: 
        #         return

        #     if root == p and self.seenp == False:
        #         self.lca_so_far = copy.deepcopy(p) 
        #         self.seenp = True
            
        #     if root == q and self.seenq == False: 
        #         self.lca_so_far = copy.deepcopy(q) 
        #         self.seenq = True 
            
        #     print(self.lca_so_far.val, self.seenp, self.seenq)
        #     dfs(root.left)
        #     dfs(root.right)

        #     if self.seenp and seenq :
        #         self.lca_so_far = root 
        # dfs(root)
        # return self.lca_so_far
        
        # # return res if res else root
             