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

# Alternative solution

class Solution1:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        node1 = headA
        node2 = headB
        while node1 != node2:
            node1 = node1.next if node1 else headB
            node2 = node2.next if node2 else headA
        return node1
