# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0 or lists is None: return
        if len(lists) == 1:
            return lists[0]
        if len(lists) == 2:
            return self.merge(lists[0], lists[1])
        left = 0
        right = len(lists) - 1
        mid = (right + left) // 2
        list1 = self.mergeKLists(lists[:mid])
        list2 = self.mergeKLists(lists[mid:])
        return self.merge(list1, list2)
        
    def merge(self, l1, l2):
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        if l1.val <= l2.val:
            l1.next = self.merge(l1.next, l2)
            return l1
        if l1.val > l2.val:
            l2.next = self.merge(l1, l2.next)
            return l2

# Alternative solution

class Solution1:
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
