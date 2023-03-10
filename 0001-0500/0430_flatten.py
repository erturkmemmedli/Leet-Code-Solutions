"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return
        Head, Tail = self.dfs(head)
        return Head
        
    def dfs(self, node):
        head = node
        temp = node
        while temp:
            if temp.child:
                h, t = self.dfs(temp.child)
                temp.child = None
                if temp.next:
                    t.next = temp.next
                    t.next.prev = t
                    temp.next = h
                    h.prev = temp
                    temp = t.next
                else:
                    temp.next = h
                    h.prev = temp
                    tail = t
                    temp = t.next
                continue
            if temp.next is None:
                tail = temp
            temp = temp.next
        return head, tail
