# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        linked_lists = set()
        temp = headA
        while temp:
            linked_lists.add(temp)
            temp = temp.next
        temp = headB
        while temp:
            if temp in linked_lists:
                return temp
            temp = temp.next
        return
