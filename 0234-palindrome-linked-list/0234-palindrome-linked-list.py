# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        res = []

        while head: 
            res.append(head.val)
            head = head.next 
        print(res)

        if len(res) == 1: 
            return True 
        
        if len(res) == 2 and res[0] != res[1]: 
            return False
    
        i = 0 
        j = len(res) - 1

        while i < j and j > len(res) //2 : 
            if res[i] == res[j]: 
                i+=1
                j-=1
            if res[i] != res[j]:
                return False
            print(i,j)

        if len(res) % 2 == 0:  
            if i+1 == j:
                return True 
            return False
        if len(res) % 2 == 1: 
            if i == j:
                return True 
            return False