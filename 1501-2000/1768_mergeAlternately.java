class Solution {
    public String mergeAlternately(String word1, String word2) {
        int l1 = word1.length();
        int l2 = word2.length();
        String output = "";
        int len = Math.min(l1, l2);

        for (int i = 0; i < len; i++) {
            output += word1.charAt(i);
            output += word2.charAt(i);
        }

        output += (l1 >= l2 ? word1.substring(len, l1) : word2.substring(len, l2));
        return output;
    }
}
