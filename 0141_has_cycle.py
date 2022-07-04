# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def __init__(self):
        self.hashmap = {}
        
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        if head in self.hashmap:
            return True
        self.hashmap[head] = True
        return self.hasCycle(head.next)

# Alternative solution

class Solution1:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        first = head
        second = head
        while second and second.next:
            first = first.next
            second = second.next.next
            if first == second: return True
        return False

# Alternative solution

class Solution2:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next: return False
        start = head.next
        end = head.next.next
        return self.isCycle(start, end)
    
    def isCycle(self, start, end):
        if not start or not end or not end.next: return False
        if start == end: return True
        return self.isCycle(start.next, end.next.next)
