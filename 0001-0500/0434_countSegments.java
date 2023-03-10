class Solution {
    public int countSegments(String s) {
        if (s.length() == 0) {
            return 0;
        }
        String[] segments = s.split(" ");
        int count = 0;
        for (int i = 0; i < segments.length; i++) {
            if (segments[i] != "") {
                count++;
            }
        }
        return count;
    }
}
