class Solution {
    public int characterReplacement(String s, int k) {
        int[] charMap = new int[26];
        int longest = 0;
        int left = 0;
        int right = 0;
        int max;
        int sum;

        while (right < s.length()) {
            max = getMax(charMap);
            sum = getSum(charMap);
            longest = Math.max(longest, sum);

            if (sum - max < k) {
                charMap[s.charAt(right) - 'A']++;
                right++;
            } else if (charMap[s.charAt(right) - 'A'] == max) {
                charMap[s.charAt(right) - 'A']++;
                right++;
            } else {
                charMap[s.charAt(left) - 'A']--;
                left++;
            }
        }

        sum = getSum(charMap);
        longest = Math.max(longest, sum);

        return longest;
    }

    public int getMax(int[] charMap) {
        int max = 0;
        for (int i = 0; i < 26; i++) max = Math.max(max, charMap[i]);
        return max;
    }

    public int getSum(int[] charMap) {
        int sum = 0;
        for (int i = 0; i < 26; i++) sum += charMap[i];
        return sum;
    }
}
