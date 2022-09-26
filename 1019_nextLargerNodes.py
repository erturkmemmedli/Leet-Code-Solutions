# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        length = self.find_length(head)
        array = [0] * length
        stack = []
        temp = head
        index = 0
        while temp:
            if not stack or stack[-1][0] >= temp.val:
                stack.append((temp.val, index))
            else:
                while stack and stack[-1][0] < temp.val:
                    val, idx = stack.pop()
                    array[idx] = temp.val
                stack.append((temp.val, index))
            index += 1
            temp = temp.next
        return array
        
    def find_length(self, head):
        count = 0
        temp = head
        while temp:
            count += 1
            temp = temp.next
        return count
