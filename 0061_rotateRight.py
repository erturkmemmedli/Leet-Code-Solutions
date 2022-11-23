# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head: return
        temp, length, last = head, 0, None
        while temp:
            if temp.next is None: last = temp
            length, temp = length + 1, temp.next
        temp, i = head, length - k % length
        while i > 1:
            temp, i = temp.next, i - 1
        if not temp.next: return head
        newHead = temp.next
        temp.next = None
        last.next = head
        return newHead
