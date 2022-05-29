# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def __init__(self):
        self.count = 0
        self.output = []
        self.stack = []
        self.node = None
        
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        self.recursive(head, k)
        self.output.append(None)
        for i in range(len(self.output)-1):
            self.output[i].next = self.output[i+1]
        return self.output[0]
        
    def recursive(self, head, k):
        if self.count == k:
            self.stack = self.stack[::-1]
            self.output += self.stack
            self.count = 0
            self.stack = []
        if head is None:
            self.output += self.stack
            return
        self.stack.append(head)
        self.count += 1
        self.recursive(head.next, k)
        return
