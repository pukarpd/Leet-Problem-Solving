# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        
        self.xFact = []
        self.yFact = []
        def dfs(root, x, y, parent, depth): 
            if not root: 
                return None 
            depth += 1 
            parentpass = root if root else  None
            dfs(root.left, x, y, parentpass, depth)
            dfs(root.right, x, y, parentpass, depth)
            if root.val == x: 
                self.xFact.append(parent)
                self.xFact.append(depth)
            if root.val == y: 
                self.yFact.append(parent)
                self.yFact.append(depth)
            depth -=1 
        dfs(root, x, y, None, 0)
        return (self.xFact[0] != self.yFact[0] and self.xFact[1] == self.yFact[1])













        # self.xFound = [0,0, False]
        # self.yFound = [0,0, False]
        # self.precursor = None 
        # self.depth = 0 
        # def dfs(root, x, y): 
        #     if not root: 
        #         return 
        #     self.depth += 1
        #     if root.left: 
        #         if root.left.val == x: 
        #             self.xFound[0] = root.val
        #             self.xFound[1] = self.depth
        #             self.xFound[2] = True 
        #     if root.right: 
        #         if root.right.val == x: 
        #             self.xFound[0] = root.val
        #             self.xFound[1] = self.depth
        #             self.xFound[2] = True 
        #     if root.left: 
        #         if root.left.val == y: 
        #             self.yFound[0] = root.val
        #             self.yFound[1] = self.depth
        #             self.yFound[2] = True 
        #     if root.right: 
        #         if root.right.val == y: 
        #             self.yFound[0] = root.val
        #             self.yFound[1] = self.depth 
        #             self.yFound[2] = True 
        #     self.precursor = root.val
        #     dfs(root.left, x, y)
        #     dfs(root.right, x, y)
        #     if root.val == x: 
        #         self.xFound[0] = self.precursor
        #         self.xFound[1] = self.depth
        #         self.xFound[2] = True 
        #     if root.val == y: 
        #         self.yFound[0] = self.precursor
        #         self.yFound[1] = self.depth
        #         self.yFound[2] = True 
        #     self.depth -=1 

        # dfs(root, x, y)
        # print(self.xFound[0], self.yFound[0], self.xFound[1], self.yFound[1])
        # return (self.xFound[0] != self.yFound[0] and self.xFound[1] == self.yFound[1])

