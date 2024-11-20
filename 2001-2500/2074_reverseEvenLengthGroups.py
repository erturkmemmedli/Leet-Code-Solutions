# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = self.find_length(head)
        group_length = 1
        prev, curr = None, head

        while length > group_length:
            length -= group_length
            if group_length % 2 == 1:
                prev, curr = self.traverse_odd(prev, curr, group_length)
            else:
                new_head, next_node = self.reverse(curr, group_length)
                prev.next = new_head
                curr.next = next_node
                prev = curr
                curr = next_node
            group_length += 1
        
        if length % 2 == 1:
            prev, curr = self.traverse_odd(prev, curr, length)
        else:
            new_head, next_node = self.reverse(curr, length)
            prev.next = new_head
            curr.next = next_node
            prev = curr
            curr = next_node

        return head
        
    def find_length(self, head):
        l, temp = 0, head
        while temp:
            temp = temp.next
            l += 1
        return l

    def traverse_odd(self, prev, curr, length):
        for _ in range(length):
            prev = curr
            curr = curr.next
        return prev, curr

    def reverse(self, node, length):
        prev, curr = None, node
        for _ in range(length):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev, curr
