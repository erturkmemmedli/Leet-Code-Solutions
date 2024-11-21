import java.math.BigInteger;

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
    public ListNode doubleIt(ListNode head) {
        StringBuilder numStr = new StringBuilder();
        ListNode temp = head;

        while (temp != null) {
            numStr.append(temp.val);
            temp = temp.next;
        }

        BigInteger num = new BigInteger(numStr.toString());
        num = num.multiply(BigInteger.valueOf(2));
        String doubledNum = num.toString();
        
        ListNode dummy = new ListNode();
        ListNode curr = dummy;

        for (int i = 0; i < doubledNum.length(); i++) {
            curr.next = new ListNode(Character.getNumericValue(doubledNum.charAt(i)));
            curr = curr.next;
        }

        return dummy.next;
    }
}
