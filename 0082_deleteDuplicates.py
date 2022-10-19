# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-inf)
        dummy.next = head
        prev = dummy
        temp = head
        duplicateFlag = False
        while temp:
            if temp.next and temp.next.val == temp.val:
                duplicateFlag = True
                temp = temp.next
            elif  temp.next and temp.next.val != temp.val and duplicateFlag:
                duplicateFlag = False
                prev.next = temp
                temp = temp.next
            elif temp.next and temp.next.val != temp.val and not duplicateFlag:
                prev.next = temp
                prev = temp
                temp = temp.next
            elif not temp.next and not duplicateFlag:
                prev.next = temp
                temp = temp.next
            elif not temp.next and duplicateFlag:
                prev.next = None
                temp = temp.next
        return dummy.next
