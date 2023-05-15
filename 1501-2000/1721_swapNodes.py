# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        arr = []
        temp = head

        while temp:
            arr.append(temp)
            temp = temp.next

        fir, sec = min(k - 1, len(arr) - k), max(k - 1, len(arr) - k )

        if fir == sec:
            return head

        if fir > 0:
            arr[fir - 1].next = arr[sec]

        if fir + 1 == sec:
            arr[sec].next = arr[fir]
        else:
            arr[sec].next = arr[fir + 1]
            arr[sec - 1].next = arr[fir]

        if sec + 1 < len(arr):
            arr[fir].next = arr[sec + 1]
        else:
            arr[fir].next = None

        return head if fir > 0 else arr[sec]

# Alternative solution (gives TLE error)

class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        length, temp = 0, head

        while temp:
            length, temp = length + 1, temp.next

        first, second = min(k, length - k + 1), max(k, length - k + 1)

        if first == second:
            return head

        first_prev_node = first_node = first_next_node = second_prev_node = second_node = second_next_node = None
        prev, curr, step = None, head, 1

        while curr:
            if step == first:
                first_prev_node = prev
                first_node = curr
                first_next_node = curr.next

            if step == second:
                second_prev_node = prev
                second_node = curr
                second_next_node = curr.next
                break

            prev = curr
            curr = curr.next
            step += 1

        print(first, second, first_node, second_node)

        if first_prev_node:
            first_prev_node.next = second_node

        if first_node.next == second_node:
            second_node.next = first_node
        else:
            second_node.next = first_next_node

        if first_node.next != second_node:
            second_prev_node.next = first_node

        first_node.next = second_next_node

        return head if first > 1 else second_node
