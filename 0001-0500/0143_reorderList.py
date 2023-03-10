# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head and not head.next:
            return head
        # find length of linked list
        n = 0
        temp = head
        while temp:
            n += 1
            temp = temp.next
        # find mid of linked list
        mid = (n + 1) // 2
        n = 0
        prev = None
        temp = head
        while n < mid:
            n += 1
            prev = temp
            temp = temp.next
        # seperate into two parts
        prev.next = None
        secondHead = self.reverseList(temp)
        # merge these parts
        return self.recursiveBuild(head, secondHead)

    def reverseList(self, node):
        prev = None
        curr = node
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

    def recursiveBuild(self, node1, node2):
        if not node1 and not node2:
            return
        node1.next = self.recursiveBuild(node2, node1.next)
        return node1

# Alternative solution

class Solution1:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head.next
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        temp, slow.next = slow.next, None
        secondHead = self.reverseList(temp)
        return self.recursiveBuild(head, secondHead)

    def reverseList(self, node):
        prev, curr = None, node
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
        return prev

    def recursiveBuild(self, node1, node2):
        if not node1 and not node2: return
        node1.next = self.recursiveBuild(node2, node1.next)
        return node1
