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
    public ListNode removeNodes(ListNode head) {
        List<ListNode> list = new ArrayList<>();
        ListNode temp = head;

        while (temp != null) {
            while (!list.isEmpty() && list.get(list.size() - 1).val < temp.val) {
                list.remove(list.size() - 1);
            }

            list.add(temp);
            temp = temp.next;
        }

        list.get(list.size() - 1).next = null;

        for (int i = 0;  i < list.size() - 1; i++) {
            list.get(i).next = list.get(i + 1);
        }

        return list.get(0);
    }
}
