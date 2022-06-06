# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        binary = ''
        temp = head
        while temp:
            binary += str(temp.val)
            temp = temp.next
        return int(binary, 2)
