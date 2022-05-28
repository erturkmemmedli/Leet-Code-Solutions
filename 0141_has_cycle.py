# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def __init__(self):
        self.count = 0
        self.hashmap = {}
        
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        if head in self.hashmap:
            return True
        self.hashmap[head] = self.count
        return self.hasCycle(head.next)
