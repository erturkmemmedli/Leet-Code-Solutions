# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        node = head.next
        head.next = node.next
        node.next = head
        node.next.next = self.swapPairs(head.next)
        return node

# Alternative solution

class Solution1:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        first = head
        if not first: return
        second = head.next
        if not second: return first
        node = second.next
        second.next = first
        first.next = self.swapPairs(node)
        return second

# Alternative solution

class Solution2:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for i, llist in enumerate(lists):
            if llist:
                heapq.heappush(heap, (llist.val, i))
        dummy = ListNode()
        temp = dummy
        while heap:
            val, idx = heapq.heappop(heap)
            llist = lists[idx]
            node = llist
            llist = llist.next
            node.next = None
            temp.next = node
            temp = temp.next
            if llist: 
                lists[idx] = llist
                heapq.heappush(heap, (llist.val, idx))
        return dummy.next
