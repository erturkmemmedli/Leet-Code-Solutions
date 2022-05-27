# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = self.counter(head, 1)
        for _ in range(count // 2):
            head = head.next
        return head
        
    def counter(self, head, count):
        if head is None:
            return 0
        return 1 + self.counter(head.next, count)
