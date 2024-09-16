/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode detectCycle(ListNode head) {
        if (head == null) return head;

        ListNode slow = head;
        ListNode fast = head;
        ListNode meetingPoint = null;

        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;

            if (slow == fast) {
                meetingPoint = slow;
                break;
            }
        }

        if (meetingPoint == null) return null;

        ListNode startPoint = head;

        while (startPoint != meetingPoint) {
            startPoint = startPoint.next;
            meetingPoint = meetingPoint.next;
        }

        return meetingPoint;
    }
}
