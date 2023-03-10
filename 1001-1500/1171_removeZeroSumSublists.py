# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prefixMap = {0: 0}
        index = 0
        presum = 0
        linkedList = [0]
        temp = head
        while temp:
            presum += temp.val
            index += 1
            if presum in prefixMap:
                index = prefixMap[presum]
                linkedList = linkedList[:index + 1]
                prefixMap = {key: val for val, key in enumerate(linkedList)}
            else:
                linkedList.append(presum)
                prefixMap[presum] = index
            temp = temp.next
        head = ListNode()
        dummy = head
        for i in range(1, len(linkedList)):
            dummy.next = ListNode(linkedList[i] - linkedList[i - 1])
            dummy = dummy.next
        return head.next
