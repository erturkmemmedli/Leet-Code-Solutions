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
    public ListNode insertGreatestCommonDivisors(ListNode head) {
        if (head.next == null) {
            return head;
        }

        ListNode first = head;
        ListNode second = head.next;

        while (second != null) {
            int gcd = findGCD(Math.min(first.val, second.val), Math.max(first.val, second.val));
            first.next = new ListNode(gcd);
            first.next.next = second;
            first = second;
            second = second.next;
        }
        
        return head;
    }

    public int findGCD(int a, int b) {
        while (b % a != 0) {
            int c = b % a;
            b = a;
            a = c;
        }

        return a;
    }
}
