# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        k = len(lists)
        print(k)

        arr = []
        for lis in lists: 
            head = lis
            while head: 
                arr.append(head.val)
                head = head.next
        
        arr.sort()

        dummy = ListNode()
        dumm = dummy
        for val in arr: 
            temp = ListNode(val)
            dummy.next = temp
            dummy = dummy.next
        
        return dumm.next

            