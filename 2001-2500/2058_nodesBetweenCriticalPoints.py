# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        first_index = None
        last_index = None
        min_distance = float('inf')
        max_distance = -float('inf')
        prev = head
        curr = head.next
        i = 1

        while curr.next:
            next = curr.next

            if prev.val < curr.val > next.val or prev.val > curr.val < next.val:
                if not first_index:
                    first_index = i
                if last_index:
                    distance = i - last_index
                    min_distance = min(min_distance, distance)
                    max_distance = max(max_distance, i - first_index)
                last_index = i
            
            prev = curr
            curr = next
            i += 1

        return [-1, -1] if not first_index or first_index == last_index else [min_distance, max_distance]
