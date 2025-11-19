# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
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

        