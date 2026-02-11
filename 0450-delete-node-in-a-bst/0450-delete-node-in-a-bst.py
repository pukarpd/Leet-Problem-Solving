# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        # Optimal Neetcode Solution O(n) or worst case O(2n)
        if not root: 
            return root 

        if key > root.val: 
            root.right = self.deleteNode(root.right, key)
        elif key < root.val: 
            root.left = self.deleteNode(root.left, key)
        else: 
            if not root.left: 
                return root.right 
            elif not root.right: 
                return root.left 
            
            # find min from right subtree as the in order successor. 
            cur = root.right 
            while cur.left: 
                cur = cur.left 
            root.val = cur.val 
            root.right = self.deleteNode(root.right, root.val)
        return root 


        # passed multiple test cases but faulty code, Did not want to clutter up code, eventually would have converged
        # but decided to look at the most optimal verison, iterative solution and O(1) space complexity
        # if counting recursive stack frames, more optimal but also more complex 
        # if not root: 
        #     return None 

        # # consider base case root
        # if key == root.val: 
        #     # consider another leaf case 
        #     if root.left == None and root.right == None: 
        #         return None 
        #     # replace with right
        #     if root.right: 
        #         temp = root.left
        #         temp2 = root.right.left
        #         root.right.left = root.left 
                
        # node = root 
        # prevNode = None 
        # leaf = False

        # while root: 
        #     if key > root.val: 
        #         prevNode = root
        #         root = root.right
            
        #     if key < root.val: 
        #         prevNode = root
        #         root = root.left
            
        #     if key == root.val:
        #         # consider leaf
        #         if root.left == None and root.right == None:
        #             leaf = True  
        #         root = prevNode 
        #         if leaf: 
        #             if root.right.val == key: 
        #                 root.right = None 
        #             if root.left.val == key: 
        #                 root.left = None 
        #             break
        #         if root.right.val == key: 
        #             temp = root.right.left
        #             root.right = root.right.right
        #             root.right.left = temp  
        #             print("\n",root)
        #         if root.left.val == key: 
        #             temp = root.left.left
        #             root.left = root.left.right
        #             root.left.left = temp 
        #         break
            

        # return node 


        
    
        