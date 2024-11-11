class Solution {
    public int dietPlanPerformance(int[] calories, int k, int lower, int upper) {
        int point = 0;
        int windowSum = 0;
        for (int i=0; i<k; i++) windowSum += calories[i];
        point += (windowSum > upper) ? 1 : (windowSum < lower ? -1 : 0);
        for (int i=k; i<calories.length; i++) {
            windowSum += calories[i] - calories[i-k];
            point += (windowSum > upper) ? 1 : (windowSum < lower ? -1 : 0);
        }
        return point;
    }
}
