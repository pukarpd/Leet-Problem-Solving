# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = []
        dummy = head
        while dummy: 
            res.append(dummy.val)
            dummy = dummy.next

        res = sorted(list(set(res)))
        
        d2 = ListNode(0)
        d = d2
        for i in res: 
            temp = ListNode(i)
            d.next = temp 
            d = d.next 
        
        return d2.next

