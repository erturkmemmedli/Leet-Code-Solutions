class Solution {
    public void reverseString(char[] s) {
        int x = 0;
        int y = s.length - 1;
        char temp;

        while (x < y) {
            temp = s[x];
            s[x] = s[y];
            s[y] = temp;
            x++;
            y--;
        }
    }
}
