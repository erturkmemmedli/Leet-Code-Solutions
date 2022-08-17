# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return
        odd, even, temp, reserved_head, reserved_next = head, head.next, head.next, head, head.next
        while temp:
            odd.next = temp.next
            temp = temp.next
            if not temp: break
            even.next = temp.next
            temp = temp.next
            odd = odd.next
            even = even.next
        odd.next = reserved_next
        return reserved_head
