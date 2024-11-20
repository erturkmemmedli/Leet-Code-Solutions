# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        list2_tail = None
        temp = list2

        while temp:
            list2_tail = temp
            temp = temp.next

        a_node = None
        b_node = None
        temp = list1
        i = 0

        while temp:
            if i + 1 == a:
                a_node = temp
            if i == b:
                b_node = temp.next
                break
            temp = temp.next
            i += 1

        a_node.next = list2
        list2_tail.next = b_node

        return list1
