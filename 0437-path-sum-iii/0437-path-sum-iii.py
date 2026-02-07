# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.res = 0 
        self.hashmap = {0:1}
        def dfs( root, targetSum, cursum): 
            if not root: 
                return
            
            cursum += root.val
            diff = cursum - targetSum
            self.res += self.hashmap.get(diff, 0)
            self.hashmap[cursum] = 1 + self.hashmap.get(cursum, 0)
            
            dfs(root.left, targetSum, cursum)
            dfs(root.right, targetSum, cursum)

            self.hashmap[cursum] -= 1 
        dfs(root, targetSum, 0)
        return self.res
            
            
            


