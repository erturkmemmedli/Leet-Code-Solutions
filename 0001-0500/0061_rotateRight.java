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
    public ListNode rotateRight(ListNode head, int k) {
        if (k == 0 || head == null) {
            return head;
        }

        int length = 0;
        ListNode temp = head;

        while (temp != null) {
            length++;
            temp = temp.next;
        }

        int rotate = length - (k % length);

        if (rotate == length) {
            return head;
        }

        ListNode prev = null;
        ListNode curr = head;

        while (rotate > 0) {
            prev = curr;
            curr = curr.next;
            rotate--;
        }

        prev.next = null;
        ListNode tail = curr;

        while (tail.next != null) {
            tail = tail.next;
        }

        tail.next = head;
        return curr;
    }
}
