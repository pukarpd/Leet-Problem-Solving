# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        # working solution 
        self.arr = []

        def dfs(root): 
            if not root: 
                self.arr.append("None")
                return
            
            dfs(root.left)
            dfs(root.right)

            self.arr.append(root.val)
            return
        
        dfs(p)
        p_arr = copy.deepcopy(self.arr)
        print(p_arr)
        self.arr = []
        dfs(q)
        print(self.arr)

        return p_arr == self.arr

        # Neetcode solution (More memory efficient, instead of O(p and q memory, its just the stack.))
        # if not p and not q: 
        #     return True
        
        # if not p or not q or p.val != q.val: 
        #     return False
        
        # return (self.isSameTree(p.left, q.left) and 
        # self.isSameTree(p.right,q.right))
