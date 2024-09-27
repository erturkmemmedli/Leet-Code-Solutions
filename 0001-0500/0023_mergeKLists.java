/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        PriorityQueue<ListNode> heap = new PriorityQueue<>((a, b) -> a.val - b.val);
        ListNode head = null;
        ListNode curr = null;

        for (ListNode node: lists) {
            if (node != null) {
                heap.offer(node);
            }
        }

        while (!heap.isEmpty()) {
            ListNode poppedNode = heap.poll();
            if (head == null) {
                head = poppedNode;
                curr = poppedNode;
            } else {
                curr.next = poppedNode;
                curr = curr.next;
            }
            if (poppedNode.next != null) {
                heap.offer(poppedNode.next);
            }
        }
        
        return head;
    }
}
