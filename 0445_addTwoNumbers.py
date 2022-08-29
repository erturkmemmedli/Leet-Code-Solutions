# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def __init__(self):
        self.remainder = 0
    
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        length_l1 = self.findLengthOfList(l1)
        length_l2 = self.findLengthOfList(l2)
        if length_l1 < length_l2:
            l1, l2 = l2, l1
        temp = l1
        k = abs(length_l1 - length_l2)
        for _ in range(k):
            temp = temp.next
        self.recursiveCalculationForEndinPart(temp, l2)
        if k:
            self.recursiveCalculationForLeadingPart(l1, k - 1)
        if self.remainder == 1:
            head = ListNode(1)
            head.next = l1
            return head
        else:
            return l1
            
    def recursiveCalculationForLeadingPart(self, l, k):
        if k > 0:
            self.recursiveCalculationForLeadingPart(l.next, k - 1)
        l.val += self.remainder
        if l.val == 10:
            self.remainder = 1
        else:
            self.remainder = 0
        l.val %= 10
        return         
            
    def findLengthOfList(self, llist):
        length = 0
        temp = llist
        while temp:
            length += 1
            temp = temp.next
        return length

    def recursiveCalculationForEndinPart(self, l1, l2):
        if l1.next:
            self.recursiveCalculationForEndinPart(l1.next, l2.next)
        l1.val = l1.val + l2.val + self.remainder
        if l1.val >= 10:
            self.remainder = 1
        else:
            self.remainder = 0
        l1.val %= 10
        return
