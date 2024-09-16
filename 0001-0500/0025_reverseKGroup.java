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
    public ListNode reverseKGroup(ListNode head, int k) {
        if (head == null) {
            return head;
        }

        int step = k;
        ListNode prev = null;
        ListNode curr = head;

        while (curr != null && step > 0) {
            prev = curr;
            curr = curr.next;
            step--;
        }

        prev.next = null;

        if (step > 0) {
            return head;
        } else {
            reverseList(head);
            head.next = reverseKGroup(curr, k);
            return prev;
        }
    }

    public void reverseList(ListNode node) {
        ListNode prev = null;
        ListNode curr = node;
        ListNode next;

        while (curr != null) {
            next = curr.next;
            curr.next = prev;
            prev = curr;
            curr = next;
        }
    }
}
