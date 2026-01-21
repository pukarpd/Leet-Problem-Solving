# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        #find mid-point 
        temp = head
        length = 0 
        while temp: 
            temp = temp.next
            length += 1
        middle_node = length//2  
        temp = head 
        
        # store prev values, and find the middle node
        prev_vals = [] 
        while middle_node > 0:
            prev_vals.append(temp.val)
            temp = temp.next
            middle_node -= 1
        
        # make a LL from prev vals, attatch the next node and then thats it
        dummy = ListNode()
        dummy2 = dummy
        for i in prev_vals:  
            nextNode = ListNode(i)
            dummy2.next = nextNode
            dummy2 = dummy2.next
        
        dummy2.next = temp.next
        return dummy.next
        
