# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        hashset = set(nums)
        indices = []
        temp = head
        while temp:
            indices.append(temp.val)
            temp = temp.next
        count = 0
        flag = True
        for num in indices:
            if num in hashset and flag:
                count += 1
                flag = False
            elif num in hashset:
                continue
            else:
                flag = True
        return count
