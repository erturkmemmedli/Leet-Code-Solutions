class Solution {
    public int minFlips(String target) {
        int count = 0;
        char last_bit = target.charAt(0);
        for (int i = 0; i < target.length(); i++) {
            if (last_bit == target.charAt(i)) {
                continue;
            } else {
                count++;
                last_bit = target.charAt(i);
            }
        }
        if (target.charAt(0) == '0') {
            return count;
        } else {
            return count + 1;
        } 
    }
}
