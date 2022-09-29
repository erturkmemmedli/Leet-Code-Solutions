# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        temp = head
        length = 0
        while temp:
            length += 1
            temp = temp.next
        minimum_item_count = length // k
        addition_item_can_be_added = length % k
        result = []
        temp = head
        item = head
        i = 1
        while len(result) < k:
            if i < minimum_item_count + (addition_item_can_be_added > 0):
                temp = temp.next
                i += 1
            else:
                result.append(head)
                if item:
                    item = temp.next
                    temp.next = None
                head = item
                temp = head
                addition_item_can_be_added -= 1
                i = 1
        return result
