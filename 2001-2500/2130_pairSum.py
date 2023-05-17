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
