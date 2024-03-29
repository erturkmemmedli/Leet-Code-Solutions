# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        node = head.next
        head.next = node.next
        node.next = head
        node.next.next = self.swapPairs(head.next)
        return node

# Alternative solution

class Solution1:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        first = head
        if not first: return
        second = head.next
        if not second: return first
        node = second.next
        second.next = first
        first.next = self.swapPairs(node)
        return second
