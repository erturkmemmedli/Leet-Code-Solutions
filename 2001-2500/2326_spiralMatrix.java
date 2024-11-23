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
    public int[][] spiralMatrix(int m, int n, ListNode head) {
        int[][] matrix = new int[m][n];
        boolean[][] seen = new boolean[m][n];
        int[][] directions = new int[][] {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
        int index = 0;
        boolean flag = false;
        int x = 0;
        int y = 0;
        
        while (head != null) {
            int i = directions[index][0];
            int j = directions[index][1];
            
            if (x + i < m && x + i >= 0 && y + j < n && y + j >= 0 && seen[x + i][y + j] == false) {
                matrix[x][y] = head.val;
                seen[x][y] = true;
                head = head.next;
                x += i;
                y += j;
                flag = false;
            } else {
                if (!flag) {
                    matrix[x][y] = head.val;
                    flag = true;
                } else {
                    break;
                }
                index = (index + 1) % 4;
            }
        }

        while (true) {
            int i = directions[index][0];
            int j = directions[index][1];
            
            if (x + i < m && x + i >= 0 && y + j < n && y + j >= 0 && seen[x + i][y + j] == false) {
                matrix[x][y] = -1;
                seen[x][y] = true;
                x += i;
                y += j;
                flag = false;
            } else {
               if (!flag) {
                    flag = true;
                    matrix[x][y] = -1;
                } else {
                    break;
                }
                index = (index + 1) % 4;
            }
        }

        return matrix;
    }
}
