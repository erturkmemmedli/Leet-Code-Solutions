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
    public ListNode mergeNodes(ListNode head) {
        ListNode temp = head;
        ListNode dummy = head;

        while (temp.next != null) {
            temp = temp.next;
            if (temp.val != 0) {
                dummy.val += temp.val;
            } else if (temp.next != null) {
                dummy.next = temp;
                dummy = dummy.next;
            } else {
                dummy.next = null;
            }
        }

        return head;
    }
}
