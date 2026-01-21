# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: 
            return None

        if head and not head.next: 
            return head 

        dummy = head 
        dummy2 = head.next
        this = dummy
        this2 = dummy2
        while dummy.next and dummy2.next: 
            dummy.next = dummy.next.next
            dummy2.next = dummy2.next.next
            dummy = dummy.next 
            dummy2 = dummy2.next
        dummy.next = this2

        return this 
        
