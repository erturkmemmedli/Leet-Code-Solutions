# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        position = 1
        front = None
        curr = head
        while position < left:
            front = curr
            curr = curr.next
            position += 1
        back = curr
        if not curr or not curr.next: return head
        nxt = curr.next
        while position < right:
            if nxt.next:
                temp = nxt.next
            else:
                temp = None
            nxt.next = curr
            curr = nxt
            nxt = temp
            position += 1
        if front:
            front.next = curr
        else:
            head = curr
        back.next = nxt
        return head
