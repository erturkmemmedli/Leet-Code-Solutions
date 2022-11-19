# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head
        left = right = head
        count = 0
        while right and right.next:
            right = right.next
            count += 1
        prev, curr = right, left
        for _ in range(count):
            curr.next, curr, prev = prev, curr.next, curr
        left.next = None
        curr.next = prev
        return curr

# Alternative solution

class Solution1:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head
        prev = head
        curr = head.next
        prev.next = None
        while curr and prev:
            node = curr.next
            curr.next = prev
            prev = curr
            curr = node 
        return prev
