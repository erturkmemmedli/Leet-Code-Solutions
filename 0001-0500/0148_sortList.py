# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp, length = head, 0
        while temp:
            temp, length = temp.next, length + 1
        if length <= 1:
            return head
        mid = length // 2
        prev, temp, length = None, head, mid
        while length > 0:
            prev, temp, length = temp, temp.next, length - 1
        if prev:
            prev.next = None
        A = self.sortList(head)
        B = self.sortList(temp)
        return self.merge(A, B)

    def merge(self, A, B):
        if A.val < B.val:
            head = A
            A = A.next
        else:
            head = B
            B = B.next
        temp = head
        while A and B:
            if A.val < B.val:
                temp.next = A
                A = A.next
            else:
                temp.next = B
                B = B.next
            temp = temp.next
        if A:
            temp.next = A
        if B:
            temp.next = B
        return head

# Alternative solution

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution1:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        slow, fast = head, head
        while fast and fast.next:
            prev, slow, fast = slow, slow.next, fast.next.next
        prev.next = None
        A = self.sortList(head)
        B = self.sortList(slow)
        return self.merge(A, B)

    def merge(self, A, B):
        if A.val < B.val:
            head = A
            A = A.next
        else:
            head = B
            B = B.next
        temp = head
        while A and B:
            if A.val < B.val:
                temp.next = A
                A = A.next
            else:
                temp.next = B
                B = B.next
            temp = temp.next
        if A:
            temp.next = A
        if B:
            temp.next = B
        return head
