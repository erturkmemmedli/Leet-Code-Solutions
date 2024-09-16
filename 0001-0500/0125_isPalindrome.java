class Solution {
    public boolean isPalindrome(String s) {
        int i = 0;
        int j = s.length() - 1;
        char a;
        char b;

        while (i < j) {
            while (i < j && !Character.isLetterOrDigit(s.charAt(i))) {
                i++;
            } a = Character.toLowerCase(s.charAt(i));

            while (i < j && !Character.isLetterOrDigit(s.charAt(j))) {
                j--;
            } b = Character.toLowerCase(s.charAt(j));

            if (a != b) return false;
            i++;
            j--;
        }

        return true;
    }
}
