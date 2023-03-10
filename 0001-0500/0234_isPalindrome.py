# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def isPalindrome(self, head) -> bool:
        nodes, current = self.traverse(head)
        for val in nodes:
            if val != current.val: return False
            current = current.next
        return True
        
    def traverse(self, node):
        nodes = []
        temp, prv, nxt = node, None, None
        while temp:
            nodes.append(temp.val)
            prv = nxt
            nxt = temp
            temp = temp.next
            nxt.next = prv
        return nodes, nxt
