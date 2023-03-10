# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        position = 1
        front = None
        curr = head
        while position < left:
            front = curr
            curr = curr.next
            position += 1
        back = curr
        if not curr or not curr.next: return head
        nxt = curr.next
        while position < right:
            if nxt.next:
                temp = nxt.next
            else:
                temp = None
            nxt.next = curr
            curr = nxt
            nxt = temp
            position += 1
        if front:
            front.next = curr
        else:
            head = curr
        back.next = nxt
        return head

# Alternative solution

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        currPosition = 1
        tailFromLeft = None
        reverseHead = None
        temp = head
        while currPosition < left:
            tailFromLeft = temp
            currPosition += 1
            temp = temp.next
        reverseHead = temp
        prev, curr = None, reverseHead
        while currPosition <= right:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            currPosition += 1
        if tailFromLeft:
            tailFromLeft.next = prev
        else:
            head = prev
        reverseHead.next = curr
        return head
