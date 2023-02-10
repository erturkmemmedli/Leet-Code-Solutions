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

# Alternative solution

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not k:
            return head
        length = 0
        temp = head
        while temp:
            length += 1
            temp = temp.next
        k = k % length
        if k == 0:
            return head
        rot = length - k
        temp = head
        prev = None
        while rot:
            if rot == 1:
                prev = temp
            temp = temp.next
            rot -= 1
        newHead = temp
        if prev:
            prev.next = None
        tail = None
        while temp:
            if not temp.next:
                tail = temp
            temp = temp.next
        if tail:
            tail.next = head
        return newHead
