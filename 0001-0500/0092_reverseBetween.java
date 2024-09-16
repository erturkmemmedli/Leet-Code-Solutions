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
    public ListNode reverseBetween(ListNode head, int left, int right) {
        ListNode firstTail = null;
        ListNode firstHead = null;
        ListNode secondTail = null;
        ListNode secondHead = null;
        ListNode prev = null;
        ListNode curr = head;
        int i = 1;

        while (curr != null) {
            if (i == left) {
                firstTail = prev;
                firstHead = curr;
            } 
            if (i == right) {
                secondTail = curr;
                secondHead = curr.next;
            }
            i++;
            prev = curr;
            curr = curr.next;
        }

        secondTail.next = null;
        ListNode reversed = reverseList(firstHead);

        if (firstTail != null) firstTail.next = reversed;
        else head = reversed;
        if (firstHead != secondHead) firstHead.next = secondHead;

        return head;
    }

    public ListNode reverseList(ListNode node) {
        ListNode prev = null;
        ListNode curr = node;
        ListNode next;

        while (curr != null) {
            next = curr.next;
            curr.next = prev;
            prev = curr;
            curr = next;
        }

        return prev;
    }
}

// Alternative solution

class Solution {
    public ListNode reverseBetween(ListNode head, int left, int right) {
        ListNode firstTail = null;
        ListNode firstHead = head;

        int current = 1;

        while (firstHead != null) {
            if (current < left ) {
                firstTail = firstHead;
                firstHead = firstHead.next;
            } else {
                break;
            }
            current++;
        }

        ListNode secondTail = firstTail;
        ListNode secondHead = firstHead;

        while (secondHead != null) {
            if (current <= right) {
                secondTail = secondHead;
                secondHead = secondHead.next;
            } else {
                break;
            }
            current++;
        }



        secondTail.next = null;
        ListNode reversed = reverseList(firstHead);
        if (firstTail != null) {
            firstTail.next = reversed;
        } else {
            head = reversed;
        }
        if (firstHead != secondHead) {
            firstHead.next = secondHead;
        }
        return head;
    }

    public ListNode reverseList(ListNode node) {
        ListNode prev = null;
        ListNode curr = node;
        ListNode next;

        while (curr != null) {
            next = curr.next;
            curr.next = prev;
            prev = curr;
            curr = next;
        }

        return prev;
    }
}
