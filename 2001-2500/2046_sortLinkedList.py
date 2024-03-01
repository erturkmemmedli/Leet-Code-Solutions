# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def sortLinkedList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        negative_tail = None
        negative_head = None
        positive_tail = None
        positive_head = None
        temp = head
        
        # [0,2,-5,5,10,-10]
        #    p    c

        while temp:
            next = temp.next

            if temp.val >= 0:
                if not positive_head:
                    positive_head = temp
                    positive_tail = temp
                else:
                    positive_tail.next = temp
                    positive_tail = positive_tail.next
            else:
                if not negative_tail:
                    negative_head = temp
                    negative_tail = temp
                else:
                    temp.next = negative_head
                    negative_head = temp
            
            temp = next

        if positive_tail:
            positive_tail.next = None
        
        if negative_tail:
            negative_tail.next = positive_head

        return negative_head if negative_head else head
