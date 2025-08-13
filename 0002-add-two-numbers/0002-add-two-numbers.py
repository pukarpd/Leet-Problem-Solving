# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not l1: 
            return None 
        if not l1: 
            return None
        l1cur = l1 
        l2cur = l2 

        dummy = ListNode(0)
        dummycur = dummy

        carry = 0
        # print("work")
        while l1 or l2: 
            if l1 and l2: 
                # logic
                newVal = l1.val + l2.val + carry
                digit = newVal % 10 
                carry = newVal // 10
                # movement 
                myNode = ListNode(digit)
                dummycur.next = myNode
                l1 = l1.next 
                l2 = l2.next 
                dummycur = dummycur.next

            elif l1:
                # logic 
                newVal = l1.val + carry 
                digit = newVal % 10 
                carry = newVal // 10 
                myNode = ListNode(digit)
                dummycur.next = myNode 
                l1 = l1.next
                dummycur = dummycur.next
            elif l2: 
                # logic 
                newVal = l2.val + carry 
                digit = newVal % 10 
                carry = newVal // 10 
                myNode = ListNode(digit)
                dummycur.next = myNode 
                l2 = l2.next
                dummycur = dummycur.next
            else: 
                break

            
            # print(myNode, newVal, digit, carry)
        # print(carry)

        if carry == 1: 
            dummycur.next = ListNode(carry)
            dummycur = dummycur.next

        return dummy.next


            


