class Solution {
    public int maxConsecutiveAnswers(String answerKey, int k) {
        int t = 0;
        int f = 0;
        int left = 0;
        int right = 0;
        int longest = 0;

        while (right < answerKey.length()) {
            if (answerKey.charAt(right) == 'T') {
                if (f > k && t >= k) {
                    if (answerKey.charAt(left) == 'F') f--;
                    else t--;
                    left++;
                } else {
                    t++;
                    right++;
                    System.out.println(f + " " + t);
                    longest = Math.max(longest, f + t);
                }
            } else {
                if (t > k && f >= k) {
                    if (answerKey.charAt(left) == 'F') f--;
                    else t--;
                    left++;
                } else {
                    f++;
                    right++;
                    System.out.println(f + " " + t);
                    longest = Math.max(longest, f + t);
                }
            }
        }

        longest = Math.max(longest, f + t);
        return longest;
    }
}
