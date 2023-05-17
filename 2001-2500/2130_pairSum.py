# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        l = []
        temp = head
        while temp:
            l.append(temp.val)
            temp = temp.next
        res = 0
        i, j = 0, len(l) - 1
        while i < j:
            res = max(res, l[i] + l[j])
            i += 1
            j -= 1
        return res

# Alternative solution

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        fast, slow = head, head

        while fast:
            slow = slow.next
            fast = fast.next.next

        first = head
        second = self.reverseList(slow)
        maxPairSum = 0

        while second:
            maxPairSum = max(maxPairSum, first.val + second.val)
            first = first.next
            second = second.next

        return maxPairSum

    def reverseList(self, head):
        prev = None
        curr = head
        
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        return prev
