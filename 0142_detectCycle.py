# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        nodes = set([head])
        while temp:
            temp = temp.next
            if temp in nodes:
                return temp
            nodes.add(temp)
            
# Alternative solution

class Solution1:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next or not head.next.next: return
        slow = head
        fast = head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast and slow and fast == slow:
                break
        if not fast or not fast.next: return
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow
