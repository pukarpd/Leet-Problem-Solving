# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # was close, neetcode helped reinforce how to construct recursively
        # but i figured out everything till rp, ri and lp, li. Good problem, however can be made more efficient with hashmap instead of .index.
        self.inorder_idx = {val: i for i, val in enumerate(inorder)}
        def makeTree (preorder, inorder): 
            if not preorder or not inorder: 
                return None 
            root_num = preorder[0]
            root = TreeNode(root_num)  

            parting_idx = self.inorder_idx[root_num]
            lp, li = preorder[1:parting_idx+1], inorder[0:parting_idx] 
            rp, ri = preorder[parting_idx+1:], inorder[parting_idx+1:]
            root.left = self.buildTree(lp, li)
            root.right = self.buildTree(rp, ri)


            return root 
        return makeTree(preorder, inorder)