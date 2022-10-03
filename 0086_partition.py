# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head: return
        first, second, m, n, temp = None, None, None, None, head
        while temp:
            if temp.val < x:
                if first is None:
                    first = temp
                    m = temp
                else:
                    m.next = temp
                    m = m.next
            else:
                if second is None:
                    second = temp
                    n = temp
                else:
                    n.next = temp
                    n = n.next
            temp = temp.next
        if m and n:
            m.next = second
            n.next = None
            return first
        elif m:
            m.next = None
            return first
        elif n:
            n.next = None
            return second
